import os
import csv
import shutil
import argparse

# Create an argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--ranges", nargs="+", help="The row ranges to convert, specified as start:end")
args = parser.parse_args()

# Set the directory path
parent_directory = "a:\scripts/datasetgeneration"

# Create a new directory for the files
output_directory = os.path.join(parent_directory, "output")
os.makedirs(output_directory, exist_ok=True)

# Open the CSV file for reading
with open("file_info.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

    # Skip the header row
    next(reader)

    # Loop over all rows in the CSV file
    for i, row in enumerate(reader):

        # Check if the current row should be converted based on the specified ranges
        in_range = False
        for r in args.ranges:
            start, end = map(int, r.split(":"))
            if i+1 >= start and i+1 <= end:
                in_range = True
                break

        if in_range:

            # Get the name of the file
            filename = row[0]

            # Construct the path to the PNG file
            png_path = row[1]

            # Construct the path to the TXT file
            txt_path = row[2]

            # Get the contents of the TXT file
            txt_contents = row[3]

            # Copy the PNG file to the output directory
            shutil.copy(png_path, output_directory)

            # Write the text contents to the TXT file in the output directory
            with open(os.path.join(output_directory, os.path.splitext(filename)[0] + ".txt"), "w") as txt_file:
                txt_file.write(txt_contents)
#python generatedatasetfromcsv.py -r 1:50 60:100
