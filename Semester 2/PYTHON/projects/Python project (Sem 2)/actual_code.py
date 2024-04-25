import pandas as pd
import matplotlib.pyplot as plt

# Set options to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Rest of your code
# ...
# Function to read data from CSV file
def read_data_from_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("CSV file not found.")
        return None

# Display records from the DataFrame
def display_records():
    file_path = 'supermarket.csv'  # Update file path as needed
    df = read_data_from_csv(file_path)
    if df is not None:
        print(df)

# Comparison chart: Cost vs MRP
def cost_vs_mrp():
    file_path = 'supermarket.csv'  # Update file path as needed
    df = read_data_from_csv(file_path)
    if df is not None:
        plt.bar(df['Total'], df['cogs'], width=0.5, color='blue')  # Using Total and cogs columns for illustration
        plt.xlabel('Total')
        plt.ylabel('Cost Price')
        plt.title('Cost vs MRP')
        plt.show()

# Comparison chart: Cost vs Total Units Sold
def cost_vs_total_units_sold():
    file_path = 'supermarket.csv'  # Update file path as needed
    df = read_data_from_csv(file_path)
    if df is not None:
        plt.bar(df['Quantity'], df['cogs'], width=0.5, color='green')  # Using Quantity and cogs columns for illustration
        plt.xlabel('Total Units Sold')
        plt.ylabel('Cost Price')
        plt.title('Cost vs Total Units Sold')
        plt.show()

# Comparison chart: Total Units Imported vs Total Units Sold
def total_units_imported_vs_sold():
    file_path = 'supermarket.csv'  # Update file path as needed
    df = read_data_from_csv(file_path)
    if df is not None:
        plt.plot(df['Quantity'], df['Quantity'], marker='o', linestyle='-', color='red')  # Using Quantity for both axes for illustration
        plt.xlabel('Total Units Imported')
        plt.ylabel('Total Units Sold')
        plt.title('Total Units Imported vs Total Units Sold')
        plt.show()

def menu():
    while True:
        print()
        print("1. Display Records")
        print("2. Cost Vs MRP")
        print("3. Cost Vs Total Goods Sold")
        print("4. Total Good Imported Vs Total Goods Sold")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_records()
        elif choice == 2:
            cost_vs_mrp()
        elif choice == 3:
            cost_vs_total_units_sold() 
        elif choice == 4:
            total_units_imported_vs_sold()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Start the menu
menu()
