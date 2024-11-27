import json
from pathlib import Path

# Input and output paths
input_filepath = Path('C:/work/law-llm/Data/processed_data_chatml.jsonl')
output_filepath = Path('C:/work/law-llm/Data/processed_data.json')

try:
    # Read JSONL and convert to JSON array
    json_array = []
    with open(input_filepath, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            json_array.append(json.loads(line))
    
    # Write as JSON array
    with open(output_filepath, 'w', encoding='utf-8') as output_file:
        json.dump(json_array, output_file, ensure_ascii=False, indent=4)
    
    print(f"Successfully converted to JSON format at: {output_filepath}")

except Exception as e:
    print(f"An error occurred: {e}")