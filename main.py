import csv
import random

# Set the number of rows for the CSV
NUM_ROWS = 100

# Define the column names
COLUMNS = ['red_shape', 'green_shape', 'white_shape', 'match']

# Define the output CSV file
PATH_TO_CSV = 'practiceTrialData.csv'

# Generate data and write to CSV
with open(PATH_TO_CSV, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(COLUMNS)  # Write the column headers

    for _ in range(NUM_ROWS):
        red_shape = random.randint(1, 10)
        green_shape = random.randint(1, 10)
        white_shape = green_shape if random.random() < 0.5 else random.randint(1, 10)
        match = int(green_shape == white_shape)  # 1 if match, 0 if not match

        writer.writerow([red_shape, green_shape, white_shape, match])