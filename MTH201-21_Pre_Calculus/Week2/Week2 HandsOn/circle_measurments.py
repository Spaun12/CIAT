#Michael Connell Jr.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

def get_float_input(prompt):
    """Utility function to handle float input with error checking."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_yes_no_input(prompt):
    """Utility function to handle yes/no input with error checking."""
    while True:
        response = input(prompt).lower()
        if response in ['yes', 'no']:
            return response
        else:
            print("Please enter 'yes' or 'no'.")

# Constants
pi = 3.14159

# Ask for initial diameter with validation
diameter_input = get_float_input("Enter the diameter of the circle in cm: ")
radius_input = diameter_input / 2  # Calculate radius from diameter

# Ask for custom area increase factor
use_custom_factor = get_yes_no_input("Would you like to set a custom area increase factor? (yes/no [default doubles diameter, quadrupling area]): ")
if use_custom_factor == 'yes':
    custom_factor = get_float_input("Enter the desired area increase factor (e.g., 2 for doubling): ")
    area_increase_factor = custom_factor
    radius_doubled = np.sqrt(area_increase_factor) * radius_input
    diameter2 = radius_doubled * 2
else:
    diameter2 = diameter_input * 2
    radius_doubled = diameter2 / 2
    area_increase_factor = 4

# Calculate areas
area1 = pi * (radius_input ** 2)
area2 = pi * (radius_doubled ** 2)

# Optionally save to Excel
save_to_excel = get_yes_no_input("Do you want to save the results to an Excel file? (yes/no): ")
if save_to_excel == 'yes':
    # Creating a DataFrame
    data = {
        'Diameter (cm)': [diameter_input, diameter2],
        'Radius (cm)': [radius_input, radius_doubled],
        'Area (cm^2)': [area1, area2]
    }

    df = pd.DataFrame(data)

    # File path with a timestamp to avoid overwriting
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"circle_measurements_{timestamp}.xlsx"
    file_path = rf"C:\Users\mdcte\OneDrive\Computer learning\CIAT1\CIAT2\MTH201-21_Pre_Calculus\Week2\Week2 HandsOn\{filename}"

    df.to_excel(file_path, index=False)
    print(f"File saved to: {file_path}")
else:
    print("Results will not be saved to an Excel file.")

print(f"Area Increase Factor: {area_increase_factor}")

# Generate points for circles using numpy
angle = np.linspace(0, 2 * np.pi, 100)

# Original circle
x_original = radius_input * np.cos(angle)
y_original = radius_input * np.sin(angle)

# Circle with adjusted area
x_doubled = radius_doubled * np.cos(angle)
y_doubled = radius_doubled * np.sin(angle)

# Plotting
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.plot(x_original, y_original, label='Original Circle')
plt.title('Original Circle')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')

plt.subplot(1, 2, 2)
plt.plot(x_doubled, y_doubled, color='r', label=f'Circle with Area Increase Factor: {area_increase_factor}')
plt.title('Adjusted Circle')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')

plt.tight_layout()
plt.show()
