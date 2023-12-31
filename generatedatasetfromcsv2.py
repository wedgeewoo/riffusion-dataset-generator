import os
import shutil
import pandas as pd

# Set the directory path
parent_directory = "a:\scripts/datasetgeneration"

# Create a new directory for the files
output_directory = os.path.join(parent_directory, "output")
os.makedirs(output_directory, exist_ok=True)

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("file_info.csv")

# Filter the DataFrame to include only rows where the "generate" column is "y"
df = df[df["generate"] == "y"]

# Loop over the rows in the filtered DataFrame
for i, row in df.iterrows():

    # Get the name of the file
    filename = row["Name"]

    # Construct the path to the PNG file
    png_path = row["PNG Path"]

    # Construct the path to the TXT file
    txt_path = row["TXT Path"]

    # Get the contents of the TXT file
    txt_contents = row["TXT Contents"]

    # Copy the PNG file to the output directory
    shutil.copy(png_path, output_directory)

    # Write the text contents to the TXT file in the output directory
    with open(os.path.join(output_directory, os.path.splitext(filename)[0] + ".txt"), "w") as txt_file:
        txt_file.write(txt_contents)
