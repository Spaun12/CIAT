#My first Website using Python Part 2

from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the journal page
@app.route('/journal')
def journal():
    return render_template('journal.html')

# Define the route for the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get the data from the form
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Do something with the data (e.g., save it to a database)
    # ...

    # Return a response to the user
    return render_template('thankyou.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
