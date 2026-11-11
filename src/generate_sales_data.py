
"""
Project: Sales Dataset Generation for EDA
Description: Generates 100,000 sample sales transactions.
"""

from pathlib import Path

import numpy as np
import pandas as pd


# 1. Configuration
np.random.seed(42)

NUM_ROWS = 100_000


def generate_sales_data():
    """Generate and save the sales dataset."""

    try:
        print("Starting sales dataset generation...")

        # 2. Define products and categories
        products = {
            "Laptop": "Electronics",
            "Mobile": "Electronics",
            "Headphones": "Electronics",
            "Chair": "Furniture",
            "Table": "Furniture",
            "Notebook": "Stationery",
            "Pen": "Stationery",
            "Backpack": "Accessories",
            "Watch": "Accessories",
        }

        product_names = list(products.keys())

        # 3. Generate transaction details
        transaction_id = np.arange(1, NUM_ROWS + 1)

        customer_id = np.random.randint(
            1001, 5001, NUM_ROWS
        )

        product = np.random.choice(
            product_names, NUM_ROWS
        )

        category = [products[item] for item in product]

        quantity = np.random.randint(
            1, 11, NUM_ROWS
        )

        price = np.round(
            np.random.uniform(100, 5000, NUM_ROWS), 2
        )

        # 4. Generate dates between 2023 and 2024
        start_date = pd.Timestamp("2023-01-01")
        end_date = pd.Timestamp("2024-12-31")

        date = start_date + pd.to_timedelta(
            np.random.randint(
                0, (end_date - start_date).days + 1,
                NUM_ROWS
            ),
            unit="D"
        )

        # 5. Generate regions
        regions = ["North", "South", "East", "West", "Central"]

        region = np.random.choice(regions, NUM_ROWS)

        # 6. Create DataFrame
        df = pd.DataFrame({
            "transaction_id": transaction_id,
            "customer_id": customer_id,
            "product": product,
            "category": category,
            "quantity": quantity,
            "price": price,
            "revenue": np.round(quantity * price, 2),
            "date": date,
            "region": region
        })

        # 7. Introduce 5% missing values in price
        missing_price = np.random.choice(
            NUM_ROWS, int(NUM_ROWS * 0.05), replace=False
        )

        df.loc[missing_price, "price"] = np.nan
        df.loc[missing_price, "revenue"] = np.nan

        # 8. Introduce 2% missing values in region
        missing_region = np.random.choice(
            NUM_ROWS, int(NUM_ROWS * 0.02), replace=False
        )

        df.loc[missing_region, "region"] = np.nan

        # 9. Create data folder and save CSV
        project_root = Path(__file__).resolve().parent.parent

        data_folder = project_root / "data"
        data_folder.mkdir(parents=True, exist_ok=True)

        output_path = data_folder / "sales_data.csv"

        df.to_csv(output_path, index=False)

        # 10. Display execution results
        print("\nSUCCESS: Dataset generated!")
        print(f"Total rows: {len(df):,}")
        print(f"Total columns: {len(df.columns)}")
        print(f"File location: {output_path}")

        print("\nMissing values:")
        print(df.isnull().sum())

        print("\nFirst 5 records:")
        print(df.head())

        print("\nDataset information:")
        df.info()

    except (OSError, ValueError) as error:
        print(f"Dataset generation failed: {error}")
        raise

    except Exception as error:
        print(f"Unexpected error: {error}")
        raise


# Execute the program
if __name__ == "__main__":
    generate_sales_data()
