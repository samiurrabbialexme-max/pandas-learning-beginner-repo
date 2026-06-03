# Code Explanation: Pandas Basics Part 1

This document explains every major code block from the notebook in beginner-friendly language.

## 1. Importing pandas

```python
import pandas as pd
```

`pandas` is a Python library used for working with structured data such as CSV files, Excel files, JSON files, and database-like tables. The alias `pd` is the standard short name used by pandas developers.

## 2. Reading a CSV file

```python
df = pd.read_csv("data/sample_employees.csv")
print(df)
```

`pd.read_csv()` loads a CSV file into a DataFrame. A DataFrame is like a table with rows and columns. `print(df)` displays the full table in the terminal or notebook output.

## 3. Reading an Excel file

```python
df = pd.read_excel("SampleSuperstore.xlsx")
print(df)
```

`pd.read_excel()` loads data from an Excel workbook. In real projects, keep your Excel file inside the `data/` folder and use a relative path such as `data/SampleSuperstore.xlsx` instead of Google Colab paths like `/content/...`.

## 4. Reading a JSON file

```python
df = pd.read_json("data/sample_data.json")
print(df)
```

`pd.read_json()` loads JSON data into a DataFrame. JSON is common in APIs and web applications.

## 5. Creating a DataFrame manually

```python
data = {
    "Name": ["Sam", "Rabbi", "Alex"],
    "Age": [10, 20, 30],
    "City": ["Dhaka", "Chittagong", "Delhi"]
}

df = pd.DataFrame(data)
print(df)
```

Here, a Python dictionary is converted into a DataFrame. Each dictionary key becomes a column name, and each list becomes the values of that column.

## 6. Saving files

```python
df.to_csv("outputs/output.csv", index=False)
df.to_json("outputs/output.json", orient="records", indent=2)
```

`to_csv()` saves the DataFrame as a CSV file. `to_json()` saves it as a JSON file. `index=False` prevents pandas from adding an extra index column in the saved CSV file.

## 7. Viewing first and last rows

```python
df.head(10)
df.tail(10)
```

`head(n)` displays the first `n` rows. `tail(n)` displays the last `n` rows. These are useful for quickly checking whether data loaded correctly.

## 8. Understanding dataset structure

```python
df.info()
```

`info()` shows column names, non-null counts, data types, and memory usage. It is useful for checking missing values and data type problems.

## 9. Descriptive statistics

```python
df.describe()
```

`describe()` returns statistical summaries for numeric columns, including count, mean, standard deviation, minimum, maximum, and quartiles.

## 10. Shape and columns

```python
print(df.shape)
print(df.columns)
```

`shape` returns the number of rows and columns in the format `(rows, columns)`. `columns` returns all column names.

## 11. Selecting one column

```python
names = df["Name"]
print(names)
```

Selecting one column returns a pandas Series. A Series is like a single column from a DataFrame.

## 12. Selecting multiple columns

```python
subset = df[["Name", "Salary"]]
print(subset)
```

To select multiple columns, use double square brackets. The inner list contains column names, and the outer brackets select those columns from the DataFrame.

## 13. Filtering rows with one condition

```python
high_salary = df[df["Salary"] > 50000]
```

This keeps only rows where the `Salary` value is greater than `50000`.

## 14. Filtering rows with AND condition

```python
filtered = df[(df["Age"] > 30) & (df["Salary"] > 50000)]
```

The `&` operator means AND. Both conditions must be true for a row to be selected. Each condition should be wrapped in parentheses.

## 15. Filtering rows with OR condition

```python
filtered = df[(df["Age"] > 30) | (df["Salary"] > 50000)]
```

The `|` operator means OR. A row is selected if at least one condition is true.

## Important correction

In pandas, multiple columns must be selected like this:

```python
df[["Column1", "Column2"]]
```

Not like this:

```python
df["Column1", "Column2"]
```

The second version will cause an error because pandas expects a single column name or a list of column names.
