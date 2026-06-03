"""
Pandas Beginner Practice - Part 1

This script demonstrates basic pandas syntax:
1. Importing pandas
2. Reading CSV and JSON files
3. Creating a DataFrame manually
4. Saving DataFrames
5. Exploring a dataset with head, tail, info, describe, shape, and columns
6. Selecting columns
7. Filtering rows with single and multiple conditions
"""

from pathlib import Path
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = ROOT_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def read_files_demo() -> None:
    """Read CSV and JSON files into pandas DataFrames."""
    employees_df = pd.read_csv(DATA_DIR / "sample_employees.csv")
    print("\nCSV DataFrame:")
    print(employees_df)

    json_df = pd.read_json(DATA_DIR / "sample_data.json")
    print("\nJSON DataFrame:")
    print(json_df)


def save_files_demo() -> None:
    """Create a DataFrame and save it as CSV and JSON."""
    data = {
        "Name": ["Sam", "Rabbi", "Alex"],
        "Age": [10, 20, 30],
        "City": ["Dhaka", "Chittagong", "Delhi"],
    }

    df = pd.DataFrame(data)
    print("\nCreated DataFrame:")
    print(df)

    df.to_csv(OUTPUT_DIR / "output.csv", index=False)
    df.to_json(OUTPUT_DIR / "output.json", orient="records", indent=2)
    print("\nFiles saved inside the outputs/ folder.")


def explore_dataset_demo() -> None:
    """Use common methods to understand a dataset."""
    df = pd.read_csv(DATA_DIR / "sample_employees.csv")

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nLast 5 rows:")
    print(df.tail())

    print("\nDataset information:")
    print(df.info())

    print("\nDescriptive statistics:")
    print(df.describe())

    print("\nShape:", df.shape)
    print("Columns:", list(df.columns))


def select_columns_demo() -> None:
    """Select one or multiple columns from a DataFrame."""
    df = pd.read_csv(DATA_DIR / "sample_employees.csv")

    names = df["Name"]
    print("\nSingle column - Name:")
    print(names)

    subset = df[["Name", "Salary"]]
    print("\nMultiple columns - Name and Salary:")
    print(subset)


def filter_rows_demo() -> None:
    """Filter rows using boolean conditions."""
    df = pd.read_csv(DATA_DIR / "sample_employees.csv")

    high_salary = df[df["Salary"] > 50000]
    print("\nEmployees with salary greater than 50000:")
    print(high_salary)

    age_and_salary = df[(df["Age"] > 30) & (df["Salary"] > 50000)]
    print("\nEmployees with age > 30 AND salary > 50000:")
    print(age_and_salary)

    age_or_salary = df[(df["Age"] > 30) | (df["Salary"] > 50000)]
    print("\nEmployees with age > 30 OR salary > 50000:")
    print(age_or_salary)


if __name__ == "__main__":
    read_files_demo()
    save_files_demo()
    explore_dataset_demo()
    select_columns_demo()
    filter_rows_demo()
