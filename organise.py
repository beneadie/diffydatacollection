import os
import glob

def append_files_to_one(input_directory, output_file):
    # Get a list of all files in the directory
     files = glob.glob(os.path.join(input_directory, '*'))

    # Open the output file in append mode
     with open(output_file, 'a') as outfile:
          for file_path in files:
               # Check if it's a file
               if os.path.isfile(file_path):
                    with open(file_path, 'r') as infile:
                         # Read the content of the file and append it to the output file
                         content = infile.read()
                         outfile.write(content)
                         # Optionally, add a newline to separate contents of different files
                         outfile.write('\n')

# Example usage
input_directory = 'cities'
output_file = 'cities_tax.py'
#append_files_to_one(input_directory, output_file)


def convert_python_to_txt(python_file_path, txt_file_path):
     # Read the content of the Python file
     with open(python_file_path, 'r') as python_file:
          content = python_file.read()

     # Get the name of the file without the extension
     file_name = python_file_path.split('/')[-1].split('.')[0]

     # Replace all instances of "dicto" with the file name
     modified_content = content.replace('taxdict', file_name)

     # Write the modified content to a text file
     with open(txt_file_path, 'w') as txt_file:
          txt_file.write(modified_content)

# Example usage
python_file_path = 'path/to/your/python_file.py'
txt_file_path = 'path/to/your/output_file.txt'
convert_python_to_txt(python_file_path, txt_file_path)
