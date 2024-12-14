# Legal Q&A Dataset Generator

A powerful tool designed to automatically generate high-quality question-answer pairs from legal documentation, specifically optimized for training and fine-tuning Large Language Models (LLMs) in the legal domain.

## Overview

This project automates the extraction of question-answer pairs from legal documentation in markdown format. It uses advanced language models to:
1. Extract relevant questions from legal text
2. Generate comprehensive, legally-sound answers
3. Format the data for various LLM fine-tuning platforms (OpenAI, Azure OpenAI, PaLM 2, Anyscale)

## Features

- **Smart Text Processing**: Automatically splits large documents into processable chunks while maintaining context
- **Token-Aware Processing**: Built-in token counting and management for optimal model interaction
- **Concurrent Processing**: Asynchronous processing of files for improved performance
- **Multiple Output Formats**: Supports various fine-tuning formats including OpenAI, Azure OpenAI, PaLM 2, and Anyscale
- **Progress Tracking**: Real-time progress monitoring for large document processing
- **Caching**: Intermediate results are cached to prevent redundant processing

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd law-llm
```

2. Install required packages:
```bash
pip install tiktoken openai langchain aiolimiter tenacity
```

## Usage

1. Place your legal markdown documents in the input directory
2. Configure the paths in `question_extractor.py`:
```python
input_directory = Path('path/to/your/markdown/files')
output_filepath = Path('path/to/output/questions.json')
```

3. Run the extraction:
```bash
python question_extractor.py
```

4. Convert the output to your desired fine-tuning format:
```bash
python fine_tune_prep.py
```

## Configuration

- **Maximum Q&A Pairs**: Default limit of 300 pairs per file (configurable in `process_file()`)
- **Token Limits**: Configured for models with 128,000 token limit
- **Rate Limiting**: Default concurrent request limit of 75% of the model's rate limit

## Output Format

The generated dataset follows this structure:
```json
[
  {
    "source": "file_path",
    "question": "What is the legal requirement for...",
    "answer": "According to the legal documentation..."
  }
]
```

## Fine-tuning Formats

Supports multiple output formats:
- **OpenAI/Anyscale**: ChatML format with system, user, and assistant messages
- **Azure OpenAI**: Simple prompt-completion pairs
- **PaLM 2**: Input-output text pairs

## Performance

- Average question size: 15.28 tokens
- Average answer size: 94.78 tokens
- Question-to-text ratio: 14% (questions generated relative to input text size)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


