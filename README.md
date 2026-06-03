# Pandas Beginner Practice - Part 1

A beginner-friendly pandas learning repository covering basic syntax, file reading/writing, dataset exploration, column selection, and row filtering.

This project is suitable for a **data analysis learning portfolio** because it shows foundational pandas skills with clean code, explanations, and runnable examples.

## Topics Covered

- Importing pandas
- Reading CSV files
- Reading JSON files
- Reading Excel files conceptually
- Creating DataFrames from dictionaries
- Saving DataFrames as CSV and JSON
- Exploring datasets with `head()`, `tail()`, `info()`, and `describe()`
- Checking dataset shape and column names
- Selecting single and multiple columns
- Filtering rows using single and multiple conditions
- Using AND `&` and OR `|` operators in pandas filters

## Repository Structure

```text
pandas-beginner-learning-repo/
│
├── data/
│   ├── sample_employees.csv
│   └── sample_data.json
│
├── docs/
│   └── CODE_EXPLANATION.md
│
├── notebooks/
│   ├── pandas_part_1_original.ipynb
│   └── pandas_part_1_cleaned.ipynb
│
├── outputs/
│   └── .gitkeep
│
├── src/
│   └── pandas_basics.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pandas-beginner-learning-repo.git
cd pandas-beginner-learning-repo
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Python script

```bash
python src/pandas_basics.py
```

### 5. Open the notebook

```bash
jupyter notebook notebooks/pandas_part_1_cleaned.ipynb
```

## Dataset Description

The sample employee dataset contains the following columns:

| Column | Meaning |
|---|---|
| Name | Employee name |
| Age | Employee age |
| City | Employee city |
| Salary | Employee salary |
| Performance Score | Employee performance score |

## Main Learning Outcomes

After completing this project, you should be able to:

1. Load structured data into pandas.
2. Create a DataFrame manually.
3. Save DataFrames into common file formats.
4. Inspect dataset structure and summary statistics.
5. Select columns from a DataFrame.
6. Filter rows based on conditions.
7. Write beginner-level pandas code in a clean GitHub-friendly format.

## Code Explanation

A detailed explanation of each code block is available here:

[Code Explanation](docs/CODE_EXPLANATION.md)

## Example Code

```python
import pandas as pd

df = pd.read_csv("data/sample_employees.csv")

high_salary = df[df["Salary"] > 50000]
print(high_salary)
```

This code reads the employee dataset and filters employees whose salary is greater than `50000`.

## Next Steps

To improve this project, you can add:

- Missing value handling
- Sorting data
- Grouping with `groupby()`
- Data visualization using Matplotlib
- A small exploratory data analysis report
- SQL practice using the same dataset

## Author

**Samiur / Alex**  
Computer Science and Engineering Graduate | AI & Data Enthusiast

## License

This project is open-source and available for learning and portfolio use.
