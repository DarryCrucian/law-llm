
# Question Extractor for Legal Documentation

This project is designed to automate the extraction of question-and-answer (Q&A) pairs from a set of markdown (`.md`) legal documents. These Q&A pairs are then used to train legal-focused large language models (LLMs), enabling them to perform better in the legal domain by enhancing their understanding of complex legal concepts, terminology, and procedural rules.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Inner Workings](#inner-workings)
- [Applications](#applications)
- [Troubleshooting](#troubleshooting)

---

## Introduction

The goal of this project is to streamline the process of preparing legal data for training large language models (LLMs). By feeding legal documents into this script, you can generate high-quality question-and-answer pairs automatically. These pairs can then be used to fine-tune or improve legal AI models, making them more adept at understanding the intricacies of legal documentation.

The application is designed with a focus on handling large volumes of text in markdown format. It ensures that the questions extracted from the documents are relevant, comprehensive, and suitable for training an LLM in the legal domain. This tool is especially helpful for legal professionals, researchers, and AI engineers working on AI solutions for law firms, legal research, or automated legal assistance systems.

---

## Installation

Before using the tool, you'll need to install the necessary Python packages:

1. **tiktoken** - The OpenAI tokenizer used to count tokens and ensure token limits are respected.
   ```bash
   pip install tiktoken
   ```

2. **openai** - The official OpenAI API client used to interact with OpenAI's models.
   ```bash
   pip install openai
   ```

3. **langchain** - A framework that helps manage, combine, and use LLMs and other utilities seamlessly.
   ```bash
   pip install langchain
   ```

4. **Pathlib** - For efficient file handling and directory management (included in Python 3 by default).

---

## Usage

### Step 1: Set Up API Key
Ensure you have your [OpenAI API key](https://platform.openai.com/account/api-keys) ready. Place the key in your environment variables, or set it directly within the codebase under `question_extractor/__init__.py`.

```bash
export OPENAI_API_KEY="your-api-key"
```

### Step 2: Configure File Paths
Set the relevant file paths in the `question_extractor.py` file (both the input folder and the output path).

### Step 3: Run the Script
To run the code, execute the following command:

```bash
python3 question_extractor.py
```

Once it is done, all questions and answers will be written as a `.json` file in the output path.

---

## Inner Workings

The code loops through all files in the specified input directory. For each file, it extracts a list of questions using the following prompt followed by a chunk of text:

```
You are an expert user extracting information to quiz people on documentation. You will be passed a page extracted from the documentation, write a numbered list of questions that can be answered based *solely* on the given text.
```

It then loops through the questions, producing an answer by passing the following prompt, along with a chunk of text and a question:

```
You are an expert user answering questions. You will be passed a page extracted from a documentation and a question. Generate a comprehensive and informative answer to the question based *solely* on the given text.
```

Most of the actual logic of the code is dedicated to processing the files concurrently (for speed) and ensuring that text chunks passed to the model are small enough to leave enough tokens for answering. If a text is too long to be sent to the model, it is split along its highest markdown heading level, and this process can be repeated recursively until we get down to single paragraphs.

---

## Applications

This tool is invaluable for legal professionals and AI researchers looking to create sophisticated AI models for the legal field. By training LLMs with high-quality Q&A pairs, the models can learn to interpret legal language, improve their understanding of legal processes, and provide more accurate responses to queries related to legal documentation.

Potential applications include:

- **Legal Research**: Facilitating faster and more efficient legal research by providing models that understand legal texts.
- **Automated Legal Assistance**: Enabling AI systems to provide legal advice or assistance in a more reliable manner.
- **Training and Education**: Helping law students and professionals learn about legal concepts and terminology through interactive Q&A.

---

## Troubleshooting

If you encounter any issues while running the script, consider the following steps:

1. **Check API Key**: Ensure that your OpenAI API key is correctly set in your environment.
2. **File Permissions**: Make sure you have the necessary permissions to read from the input directory and write to the output path.
3. **Python Environment**: Verify that you have all the required packages installed and that you are using a compatible version of Python.
4. **Input Directory**: Confirm that the specified input directory contains valid markdown files for processing.

For any additional help or suggestions, please feel free to open an issue on the project's GitHub repository.
