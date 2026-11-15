# Task 5: Data Analysis on CSV Files

## Objective
Analyzed sales data using Python and Pandas to extract basic data insights and visualize sales trends.

## Tools Used
- **Python** (Managed via `uv`)
- **Pandas** (Data manipulation)
- **Matplotlib** (Data visualization)
- **Jupyter Notebook** (Interactive coding environment)

## How to Run
This project uses `uv` for dependency management. To run the notebook locally:
1. Install `uv` if you haven't already.
2. Run `uv sync` to install dependencies.
3. Run `uv run jupyter notebook` to open the analysis notebook.

## Key Concepts Demonstrated
- Loading CSV data into a Pandas DataFrame.
- Handling missing data (`NaN`).
- Filtering rows and understanding `loc[]` vs `iloc[]`.
- Using `groupby()` and `sum()` to aggregate data.
- Creating a bar chart using `.plot()`.

## Interview Question Insights
- **Pandas:** Used for data manipulation and analysis.
- **DataFrame:** A 2-dimensional labeled data structure with columns of potentially different types.
- **groupby():** Splits the data into groups based on some criteria and applies a function to the groups.
