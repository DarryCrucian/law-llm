import json
from pathlib import Path

# Input and output paths
input_filepath = Path('C:/work/law-llm/Data/processed_data.json')
output_filepath = Path('C:/work/law-llm/Data/processed_data_chatml.jsonl')

# Get the system prompt from prompts.py
system_prompt = """Take a deep breath and think step by step as you carefully read the following legal documentation excerpt and the related question. Your role is to act as a knowledgeable lawyer, providing a comprehensive and well-reasoned answer solely based on the given text. Ensure your response is thorough, accurate, and presented with legal precision."""

# Convert to chatml format
try:
    with open(input_filepath, 'r') as input_file:
        data = json.load(input_file)
        
        with open(output_filepath, 'w', encoding='utf-8') as output_file:
            for item in data:
                chatml_format = {
                    'messages': [
                        {'role': 'system', 'content': system_prompt},
                        {'role': 'user', 'content': item['question']},
                        {'role': 'assistant', 'content': item['answer']}
                    ]
                }
                json.dump(chatml_format, output_file, ensure_ascii=False)
                output_file.write('\n')
    
    print(f"Successfully converted to chatml format at: {output_filepath}")

except Exception as e:
    print(f"An error occurred: {e}")