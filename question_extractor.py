import json
from pathlib import Path
from question_extractor import extract_questions_from_directory
import os

# Define the input and output paths
input_directory = Path(r'C:/Nous-work/work/work/mp-dataset-builder-main/mp-dataset-builder-main/question_extractor/Data')
output_filepath = Path(r'C:/Nous-work/work/work/mp-dataset-builder-main/mp-dataset-builder-main/question_extractor/processed_data/questions.json')

# Ensure the input directory exists
if not input_directory.exists():
    raise FileNotFoundError(f"Input directory {input_directory} does not exist.")

# Ensure the output directory exists, create it if not
output_directory = output_filepath.parent
if not output_directory.exists():
    print(f"Output directory {output_directory} does not exist. Creating directory.")
    os.makedirs(output_directory)

# Run the question extraction on the input directory
try:
    extracted_questions = extract_questions_from_directory(input_directory)
    
    # Save the extracted questions as a JSON file
    with open(output_filepath, 'w') as output_file:
        json.dump(extracted_questions, output_file, indent=4)
        print(f"Results have been saved to {output_filepath}.")

except PermissionError:
    print(f"Permission denied: Unable to write to {output_filepath}. Please check your file permissions.")

except Exception as e:
    print(f"An error occurred during question extraction: {e}")
