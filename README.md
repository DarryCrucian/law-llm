## Installation

Install the following Python packages
* `tiktoken`, the OpenAI tokeniser,
* `openai`, the official OpenAI API client,
* `langchain`, glue code used to combine models and utilities.

## Usage

This script is designed to turn a folder of markdown (`.md`) documents into a `.json` file containing a list of questions, answers and paths to the source documents that were used to produce them.

To run the code, set the relevant file paths in the `question_extractor.py` file (both the input folder and the output path) and insure that your [OpenAI API key](https://platform.openai.com/account/api-keys) is in the environment.
Then run the script with Python:

```
python3 question_extractor.py
```

Once it is done, all questions/answers will be written as a `.json` file in the output path.

## Inner-workings

The code loops on all files, for each file it extracts a list of questions using the following prompt followed by a chunk of text:

```
You are an expert user extracting information to quiz people on documentation. You will be passed a page extracted from the documentation, write a numbered list of questions that can be answered based *solely* on the given text.
```

It then loops on the questions, producing an answer by passing the following prompt followed by a chunk of text and a question:

```
You are an expert user answering questions. You will be passed a page extracted from a documentation and a question. Generate a comprehensive and informative answer to the question based *solely* on the given text.
```

Most of the actual logic of the code is dedicated to processing the files concurrently (for speed) and insuring that text chunks passed to the model are small enough to leave enough tokens for answering.

If a text is too long to be sent to the model, it is split along its highest markdown heading level (the process can be repeated recursively if needed until we get down to single paragraphs).



