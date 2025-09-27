import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np


def generate_sales_data():
    """
    Generate sales data from January 1, 2024 to September 27, 2025
    Matching the structure of the original tableau_sample_data.csv
    """

    # Data arrays based on your original data and dashboard
    customers = [
        "Atlantic Business Solutions",
        "Continental Corp",
        "Raymont Enterprises",
        "Vermont Manufacturing",
        "Global Supplies Inc",
        "West Coast Industries",
        "Southern Retail Group",
        "Metro Trading Co",
        "Pacific Trading Co",
        "Midwest Partners",
        "Tech Region Inc",
        "Central Sales Ltd",
        "Metro Distribution",
        "Regional Sales Network",
        "Raymond Buch",
    ]

    regions = ["Central", "Vermont", "East", "West", "North", "South", "New York City"]

    sales_reps = [
        "Frank Miller",
        "David Wilson",
        "Carol Davis",
        "Emma Brown",
        "Grace Lee",
        "Henry Taylor",
        "Alice Johnson",
        "Bob Smith",
        "John Anderson",
        "Sarah Connor",
    ]

    product_categories = [
        "Technology",
        "Furniture",
        "Office Supplies",
        "Electronics",
        "Software",
    ]

    # Date range: January 1, 2024 to September 27, 2025
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 9, 27)
    total_days = (end_date - start_date).days + 1

    print(
        f"Generating data from {start_date.strftime('%m/%d/%Y')} to {end_date.strftime('%m/%d/%Y')}"
    )
    print(f"Total days: {total_days}")

    # Generate the data
    data = []
    order_counter = 1

    # Generate approximately 15-20 orders per day
    for day_offset in range(total_days):
        current_date = start_date + timedelta(days=day_offset)
        orders_per_day = random.randint(15, 20)  # 15-20 orders per day

        for order_of_day in range(orders_per_day):
            # Generate delivery date (1-12 days after order)
            delivery_days = random.randint(1, 12)
            delivery_date = current_date + timedelta(days=delivery_days)

            # Generate order details
            quantity_sold = random.randint(1, 50)  # 1-50 units
            unit_price = round(random.uniform(50.0, 2000.0), 2)  # $50-$2000
            cost_per_unit = round(
                random.uniform(unit_price * 0.4, unit_price * 0.8), 2
            )  # 40-80% of unit price

            # Create order ID
            order_id = f"ORD-{current_date.strftime('%Y%m%d')}-{order_counter:04d}"

            order = {
                "Order_ID": order_id,
                "Order_Date": current_date.strftime("%m/%d/%Y"),
                "Delivery_Date": delivery_date.strftime("%m/%d/%Y"),
                "Customer": random.choice(customers),
                "Region": random.choice(regions),
                "Sales_Rep": random.choice(sales_reps),
                "Product_Category": random.choice(product_categories),
                "Quantity_Sold": quantity_sold,
                "Unit_Price": unit_price,
                "Cost_Per_Unit": cost_per_unit,
            }

            data.append(order)
            order_counter += 1

    # Create DataFrame
    df = pd.DataFrame(data)

    # Calculate statistics
    df["Sales"] = df["Quantity_Sold"] * df["Unit_Price"]
    df["Profit"] = df["Quantity_Sold"] * (df["Unit_Price"] - df["Cost_Per_Unit"])
    df["Days_to_Deliver"] = pd.to_datetime(df["Delivery_Date"]) - pd.to_datetime(
        df["Order_Date"]
    )
    df["Days_to_Deliver"] = df["Days_to_Deliver"].dt.days

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_quantity = df["Quantity_Sold"].sum()
    avg_days_to_ship = df["Days_to_Deliver"].mean()

    print(f"\nGenerated {len(df)} orders")
    print(f"Total Sales: ${total_sales/1000:.1f}k")
    print(f"Total Profit: ${total_profit/1000:.1f}k")
    print(f"Total Quantity: {total_quantity:,}")
    print(f"Average Days to Ship: {avg_days_to_ship:.1f} days")
    print(f"Sales per Customer: ${total_sales/len(customers):.1f}")
    print(f"Profit per Order: ${total_profit/len(df):.1f}")

    # Remove helper columns before saving
    df = df.drop(["Sales", "Profit", "Days_to_Deliver"], axis=1)

    return df


def save_to_csv(df, filename="updated_tableau_sample_data.csv"):
    """Save the generated data to CSV file"""
    df.to_csv(filename, index=False)
    print(f"\nCSV file saved as '{filename}'")
    print("File is ready for import into Tableau!")


def preview_data(df, num_rows=10):
    """Preview the generated data"""
    print("\nData Preview:")
    print("=" * 80)
    print(df.head(num_rows).to_string(index=False))
    print("\nData Info:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

    # Show date range
    min_date = pd.to_datetime(df["Order_Date"]).min()
    max_date = pd.to_datetime(df["Order_Date"]).max()
    print(
        f"Date Range: {min_date.strftime('%m/%d/%Y')} to {max_date.strftime('%m/%d/%Y')}"
    )


# Main execution
if __name__ == "__main__":
    print("Generating Sales Data for Tableau Dashboard...")
    print("=" * 50)

    # Generate the data
    sales_df = generate_sales_data()

    # Preview the data
    preview_data(sales_df)

    # Save to CSV
    save_to_csv(sales_df)

    print("\nScript completed successfully!")
    print(
        "You can now import 'updated_tableau_sample_data.csv' into Tableau to recreate your dashboard."
    )
