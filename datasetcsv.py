import os
import csv

# Set the directory path
parent_directory = "A:/io/Projects/riffusionwedgeewoo/Training-Data/dfwedgeewoobackup"



# Function to get the path of the WAV file
def get_wav_path(png_path):
    return png_path.replace(".png", ".wav")

# Open the CSV file for writing
with open("file_info.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["Name", "PNG Path", "TXT Path", "WAV Path", "TXT Contents", "generate"])

    # Loop over all directories and files in the parent directory
    for root, dirs, files in os.walk(parent_directory):

        # Loop over all files in the directory
        for filename in files:

            # Check if the file is a PNG
            if filename.endswith(".png"):

                # Construct the path to the corresponding TXT and WAV files
                png_path = os.path.join(root, filename)
                txt_path = os.path.join(root, filename.replace(".png", ".txt"))
                wav_path = get_wav_path(png_path)

                # Check if the TXT file exists
                if os.path.isfile(txt_path):

                    # Read the contents of the TXT file
                    with open(txt_path, "r") as txt_file:
                        txt_contents = txt_file.read()

                    # Write the file information to the CSV file
                    writer.writerow([filename, png_path, txt_path, wav_path, txt_contents])
