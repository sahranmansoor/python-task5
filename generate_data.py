import pandas as pd
import numpy as np

def main():
    np.random.seed(42)
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    regions = ['North', 'South', 'East', 'West']

    data = {
        'Date': pd.date_range(start='2025-01-01', periods=200, freq='D'),
        'Category': np.random.choice(categories, 200),
        'Region': np.random.choice(regions, 200),
        'Sales': np.random.uniform(50, 500, 200).round(2),
        'Quantity': np.random.randint(1, 20, 200)
    }

    # Introduce a few NaN values to demonstrate handling them (Interview Q10)
    data['Sales'][5] = np.nan
    data['Sales'][15] = np.nan

    df = pd.DataFrame(data)
    df.to_csv('sales_data.csv', index=False)
    print("sales_data.csv created successfully!")

if __name__ == "__main__":
    main()
