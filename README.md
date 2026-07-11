-> IoTQueryGPT v2.4
A GPT-style Transformer built completely from scratch using PyTorch that converts natural language IoT queries into executable SQL and runs them on a live SQLite database.

-> Project Overview
IoTQueryGPT is an end-to-end Natural Language → SQL system designed for IoT environments.
Users can enter queries such as:

show active devices

and the model generates:

SELECT * FROM devices WHERE status = 'active';

The generated SQL is then executed on a SQLite database and the results are displayed through a Streamlit web application.

-> Features
Transformer From Scratch
Custom GPT-style decoder-only Transformer
Multi-Head Self Attention
Feed Forward Networks
Positional Embeddings
Causal Masking
Autoregressive Generation
Dataset Generation Pipeline

Custom synthetic dataset generation system supporting:

Numeric Filters
Categorical Filters
Aggregations
Sorting
BETWEEN Clauses
GROUP BY
HAVING
Time-Based Queries
Multi-Condition Queries
Advanced Multi-Condition Queries
SQL Execution Engine

Generated SQL is executed against a live SQLite database containing:

IoT Devices
Sensor Readings
Evaluation Framework

Automated benchmark evaluation including:

Exact SQL Match Accuracy
Category-wise Accuracy
JSON Evaluation Reports
User Interfaces
Interactive CLI
Streamlit Web Application

-> Model Statistics
| Metric               |          Value |
| -------------------- | -------------: |
| Parameters           |    4.9 Million |
| Vocabulary Size      |            304 |
| Context Length       |            128 |
| Layers               |              6 |
| Attention Heads      |              8 |
| Embedding Size       |            256 |
| Dataset Size         | 13,411 Samples |
| Benchmark Queries    |             73 |
| Exact Match Accuracy |         82.19% |

-> Architecture

User Query
     │
     ▼
Tokenizer
     │
     ▼
MiniGPT Transformer
     │
     ▼
Generated SQL
     │
     ▼
SQLite Execution Engine
     │
     ▼
Results Table

-> Project structure

data/         → Model weights, tokenizer, datasets, benchmark reports, SQLite database
notebooks/    → Experiments and exploratory analysis
src/          → Transformer implementation, training, inference and evaluation code
generators/   → Synthetic dataset generation framework
streamlit_app.py → Web application for NL-to-SQL querying

IoTQueryGPT/
│
├── data/
│   ├── evaluation_queries.json
│   ├── evaluation_report.json
│   ├── iot_queries.txt
│   ├── iot.db
│   ├── model.pt
│   ├── tokenizer.pkl
│   └── training_info.json
│
├── notebooks/
│
├── src/
│   │
│   ├── attention.py
│   ├── multihead_attention.py
│   ├── transformer_block.py
│   ├── mlp.py
│   ├── gpt.py
│   │
│   ├── dataset.py
│   ├── train.py
│   ├── generate.py
│   ├── inference.py
│   ├── evaluate.py
│   │
│   ├── cli.py
│   ├── sql_executor.py
│   │
│   ├── create_database.py
│   ├── populate_database.py
│   ├── test_database.py
│   ├── test_executor.py
│   │
│   ├── generate_dataset.py
│   ├── generate_evaluation_set.py
│   │
│   ├── char_tokenizer.py
│   └── word_tokenizer.py
│
│   └── generators/
│       ├── __init__.py
│       ├── config.py
│       ├── helper.py
│       ├── templates.py
│       ├── sql_templates.py
│       │
│       ├── numeric.py
│       ├── categorical.py
│       ├── aggregation.py
│       ├── sorting.py
│       ├── between.py
│       ├── time_queries.py
│       ├── group_by.py
│       ├── having.py
│       ├── multi_condition.py
│       └── advanced_multi_condition.py
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore

-> Dataset
The model is trained on a custom instruction-tuning dataset generated automatically using template-based query generators.

Example:

### Instruction:
Convert the following IoT query into SQL.

### Input:
show devices with battery below 20

### Response:
SELECT * FROM devices WHERE battery < 20;

-> Supported Query Types

Numeric Queries
show sensors with temperature above 40
show devices with battery below 20

Categorical Queries
show active devices
show devices in warehouse

Aggregations
show average battery
show maximum temperature

Sorting
show top 10 devices with highest battery
show top 5 devices with lowest battery

GROUP BY
count devices by status
show average humidity by room

HAVING
show locations where average battery exceeds 60

BETWEEN
show sensors with temperature between 20 and 40

Time Queries
show devices connected today
show devices connected in the last 24 hours

Multi Condition Queries
find online devices in building A with battery greater than 60

-> Installation

Clone the repository:

git clone https://github.com/Arijit963/IoTQueryGPT.git
cd IoTQueryGPT
-------------------------------------------------------------------
Create a virtual environment:
python -m venv .venv
-------------------------------------------------------------------
Activate:

Windows
.venv\Scripts\activate
-------------------------------------------------------------------
Linux / Mac
source .venv/bin/activate
-------------------------------------------------------------------
Install dependencies:
pip install -r requirements.txt

-> Training 
Generate dataset:
python src/generate_dataset.py
-------------------------------------------------------------------
Train model:
python src/train.py

-> Evaluation
Run benchmark:
python src/evaluate.py
-------------------------------------------------------------------
Example Output:

Accuracy : 82.19%

where     : 92.31%
group_by  : 100.00%
having    : 60.00%
order_by  : 100.00%
between   : 60.00%
time      : 50.00%

-> CLI demo

Launch CLI:
python src/cli.py
-------------------------------------------------------------------
Example:

IoT Query > show active devices

Generated SQL:

SELECT * FROM devices
WHERE status = 'active';

Results:
...

-> Streamlit web app
Run locally:

streamlit run streamlit_app.py
-------------------------------------------------------------------
Features:

Natural Language Input
SQL Generation
Copy SQL
Execute Query
Interactive Results Table

-> Technologies used
Python
PyTorch
SQLite
Streamlit
Pandas
NumPy

-> Future improvements
Improve HAVING query accuracy
Improve temporal reasoning
Support JOIN operations
User-uploaded datasets
Dynamic schema detection
REST API deployment
Hugging Face deployment
Fine-tuning on real-world SQL datasets

-> Author 

Arijit Adhikary

B.Tech CSE (IoTCS)
Heritage Institute of Technology, Kolkata

GitHub: https://github.com/Arijit963/
LinkedIn : https://linkedin.com/in/arijit-adhikary-42732527a