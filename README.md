# IoTQueryGPT v2

A GPT-style Transformer built from scratch using PyTorch that converts natural language IoT queries into SQL and executes them on a live SQLite database.

## Features

- Transformer architecture from scratch
- Multi-head self-attention
- Natural language to SQL
- SQLite query execution
- Streamlit web interface

## Model

- Parameters: 4.9M
- Vocabulary Size: 283
- Accuracy: 95%

## Example

Input:

show active devices

Output:

SELECT * FROM devices WHERE status='active';