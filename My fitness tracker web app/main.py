# Import necessary modules from flask
from flask import Flask, render_template, request, redirect, url_for
# Import SQLAlchemy for database management
from flask_sqlalchemy import SQLAlchemy

# Create an instance of Flask web application
app = Flask(__name__)

# Setup the database connection configuration
# Here we are using SQLite as our database and 'database.db' as our database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# Create an instance of SQLAlchemy
db = SQLAlchemy(app)

# Define a model for 'PhysicalMetrics' which represents a database table
class PhysicalMetrics(db.Model):
    # Each attribute represents a column in the database table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each entry
    date_logged = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp of each entry
    weight = db.Column(db.Float, nullable=False)  # Weight data (in kg)
    waist_size = db.Column(db.Float, nullable=True)  # Waist size data (in cm)
    neck_size = db.Column(db.Float, nullable=True)  # Neck size data (in cm)
    calf_size = db.Column(db.Float, nullable=True)  # Calf size data (in cm)
    chest_size = db.Column(db.Float, nullable=True)  # Chest size data (in cm)
    hip_size = db.Column(db.Float, nullable=True)  # Hip size data (in cm)
    body_fat_percentage = db.Column(db.Float, nullable=True)  # Body fat percentage data (in %)
    resting_heart_rate = db.Column(db.Integer, nullable=True)  # Resting heart rate data (in bpm)
    blood_pressure_systolic = db.Column(db.Integer, nullable=True)  # Systolic blood pressure data
    blood_pressure_diastolic = db.Column(db.Integer, nullable=True)  # Diastolic blood pressure data

# Nutrition model
class Nutrition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_logged = db.Column(db.DateTime, default=datetime.utcnow)
    meal_name = db.Column(db.String(100), nullable=False)
    food_type = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    meal_time = db.Column(db.Time, nullable=False)
    water_intake = db.Column(db.Float)

# Exercise model
class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_logged = db.Column(db.DateTime, default=datetime.utcnow)
    exercise_name = db.Column(db.String(100), nullable=False)
    exercise_type = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration of the exercise in minutes
    intensity = db.Column(db.String(100), nullable=True)  # Optional: Intensity of the exercise (e.g., Light, Moderate, High)
    distance = db.Column(db.Float, nullable=True)  # Optional: Distance covered in the exercise (e.g., miles)

# Create all database tables according to the models defined
db.create_all()

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    # If the request is POST, it means user has submitted the weight
    if request.method == 'POST':
        # Get the value from each form field
        weight = request.form.get('weight')
        waist_size = request.form.get('waist_size')
        neck_size = request.form.get('neck_size')
        calf_size = request.form.get('calf_size')
        chest_size = request.form.get('chest_size')
        hip_size = request.form.get('hip_size')
        body_fat_percentage = request.form.get('body_fat_percentage')
        resting_heart_rate = request.form.get('resting_heart_rate')
        blood_pressure_systolic = request.form.get('blood_pressure_systolic')
        blood_pressure_diastolic = request.form.get('blood_pressure_diastolic')

        # Validate that the required values have been provided
        if weight and waist_size and neck_size and calf_size and chest_size:
            # Create a new entry for the 'PhysicalMetrics' table with these values
            new_entry = PhysicalMetrics(
                weight=weight, 
                waist_size=waist_size,
                neck_size=neck_size,
                calf_size=calf_size,
                chest_size=chest_size,
                hip_size=hip_size,
                body_fat_percentage=body_fat_percentage,
                resting_heart_rate=resting_heart_rate,
                blood_pressure_systolic=blood_pressure_systolic,
                blood_pressure_diastolic=blood_pressure_diastolic
            )
            # Add the new entry to the database session
            db.session.add(new_entry)
            # Commit the session to store the new entry in the database
            db.session.commit()
    
    # Query all the logs from the database
    weights = PhysicalMetrics.query.order_by(PhysicalMetrics.date_logged.desc()).all()
    nutrition_logs = Nutrition.query.order_by(Nutrition.date_logged.desc()).all()
    exercise_logs = Exercise.query.order_by(Exercise.date_logged.desc()).all()
    
    # Return the home page with all the logs
    return render_template(
        'index.html',
        weights=weights,
        nutrition_logs=nutrition_logs,
        exercise_logs=exercise_logs
    )

# New nutrition route handler
@app.route('/nutrition', methods=['GET', 'POST'])
def nutrition():
    if request.method == 'POST':
        meal_name = request.form.get('meal_name')
        food_type = request.form.get('food_type')
        quantity = request.form.get('quantity')
        meal_time = request.form.get('meal_time')
        water_intake = request.form.get('water_intake')

        new_nutrition_log = Nutrition(
            meal_name=meal_name, 
            food_type=food_type, 
            quantity=float(quantity), 
            meal_time=meal_time, 
            water_intake=float(water_intake) if water_intake else None
        )
        db.session.add(new_nutrition_log)
        db.session.commit()
        return redirect(url_for('nutrition'))

    nutrition_logs = Nutrition.query.order_by(Nutrition.date_logged.desc()).all()
    return render_template('nutrition.html', nutrition_logs=nutrition_logs)

# New exercise route handler
@app.route('/exercise', methods=['GET', 'POST'])
def exercise():
    if request.method == 'POST':
        exercise_name = request.form.get('exercise_name')
        exercise_type = request.form.get('exercise_type')
        duration = request.form.get('duration')
        intensity = request.form.get('intensity')
        distance = request.form.get('distance')  # New line: retrieve distance from form

        new_exercise_log = Exercise(
            exercise_name=exercise_name,
            exercise_type=exercise_type,
            duration=int(duration),
            intensity=intensity if intensity else None,
            distance=float(distance) if distance else None  # New line: add distance to the new Exercise object
        )
        db.session.add(new_exercise_log)
        db.session.commit()
        return redirect(url_for('exercise'))

    exercise_logs = Exercise.query.order_by(Exercise.date_logged.desc()).all()
    return render_template('exercise.html', exercise_logs=exercise_logs)


# Run the application
# If this script is run directly (not imported), then start the application
if __name__ == '__main__':
    app.run(debug=True)
