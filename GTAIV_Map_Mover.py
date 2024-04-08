import os
import re
import sys

# The method should receive files of type .opl or .obn, and parameters defining
# increments for the X, Y and Z axes.
def process_file(input_file, output_file, increment_x, increment_y, increment_z):
    with open(input_file, 'r') as file, open(output_file, 'w') as new_file:
        for line in file:
            # In case of .opl files, each line starting with a number will have their first three numbers
            # between commas (X, Y, Z axes) incremented by the values passed as parameters.
            if input_file.endswith(".opl"):
                if re.match(r'^\s*-?\d', line): 
                    axes = line.strip().split(',')
                    axes[0] = str(float(axes[0]) + increment_x)
                    axes[1] = str(float(axes[1]) + increment_y)
                    axes[2] = str(float(axes[2]) + increment_z)
                    modified_line = ','.join(axes) + '\n'
                    new_file.write(modified_line)
                else:
                    new_file.write(line)
            # In case of .obn files, each line starting with 'Centroid' and 'VertexOffset' will have their next three numbers
            # separated by spaces (X Y Z axes) incremented by the values passed as parameters.
            elif input_file.endswith(".obn"):
                modified_line = re.sub(r'Centroid (-?\d+\.\d+) (-?\d+\.\d+) (-?\d+\.\d+)', lambda m: f'Centroid {float(m.group(1)) + increment_x} {float(m.group(2)) + increment_y} {float(m.group(3)) + increment_z}', line)
                modified_line = re.sub(r'VertexOffset (-?\d+\.\d+) (-?\d+\.\d+) (-?\d+\.\d+)', lambda m: f'VertexOffset {float(m.group(1)) + increment_x} {float(m.group(2)) + increment_y} {float(m.group(3)) + increment_z}', modified_line)
                new_file.write(modified_line)

# This method creates a 'modified_files' subdirectory in case it doesn't exist,
# processes the files to be modified located in a 'files' subdirectory
# and moves them to 'modified_files'.
def process_files_in_directory(increment_x, increment_y, increment_z):
    current_directory = os.path.join(os.getcwd(), "files")
    if not os.path.exists('modified_files'):
        os.makedirs('modified_files')
    for filename in os.listdir(current_directory):
        if filename.endswith(".opl") or filename.endswith(".obn"):
            input_file = os.path.join(current_directory, filename)
            output_file = os.path.join('modified_files', filename)
            process_file(input_file, output_file, increment_x, increment_y, increment_z)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python GTAIV_Map_Mover.py increment_x increment_y increment_z")
    else:
        increment_x = float(sys.argv[1])
        increment_y = float(sys.argv[2])
        increment_z = float(sys.argv[3])
        process_files_in_directory(increment_x, increment_y, increment_z)