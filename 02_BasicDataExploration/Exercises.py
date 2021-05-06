# Exercises
# Run the following cell to set up code-checking, which will verify your work as you go.

# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex2 import *
print("Setup Complete")

# Step 1: Loading Data
# Read the Iowa data file into a Pandas DataFrame called home_data.

import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)

# Call line below with no argument to check that you've loaded the data correctly
step_1.check()

# Step 2: Review The Data
# Use the command you learned to view summary statistics of the data. 
# Then fill in variables to answer the following questions.

# Print summary statistics in next line
home_data.describe()

# What is the average lot size (rounded to nearest integer)? Resp.:
avg_lot_size = 10517

# As of today, how old is the newest home (current year - the date in which it was built)? Resp.:
newest_home_age = 11

# Checks your answers
step_2.check()