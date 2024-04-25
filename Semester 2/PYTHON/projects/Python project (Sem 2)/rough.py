import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import subprocess

# Set options to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


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

def cost_vs_mrp(chart_type='bar'):
    file_path = 'supermarket.csv'  # Update file path as needed
    df = read_data_from_csv(file_path)
    if df is not None:
        if chart_type == 'bar':
            plt.bar(df['Total'], df['cogs'], width=0.5, color='blue')  # Using Total and cogs columns for illustration
        elif chart_type == 'line':
            plt.plot(df['Total'], df['cogs'], marker='o', linestyle='-', color='blue')
        plt.xlabel('Total')
        plt.ylabel('Cost Price')
        plt.title('Cost vs MRP')
        plt.show()

def cost_vs_total_units_sold(chart_type='bar'):
    file_path = 'supermarket.csv'  # Update file path as needed
    df = read_data_from_csv(file_path)
    if df is not None:
        if chart_type == 'bar':
            plt.bar(df['Quantity'], df['cogs'], width=0.5, color='green')  # Using Quantity and cogs columns for illustration
        elif chart_type == 'line':
            plt.plot(df['Quantity'], df['cogs'], marker='o', linestyle='-', color='green')
        plt.xlabel('Total Units Sold')
        plt.ylabel('Cost Price')
        plt.title('Cost vs Total Units Sold')
        plt.show()

def total_units_imported_vs_sold(chart_type='line'):
    file_path = 'supermarket.csv'  # Update file path as needed
    df = read_data_from_csv(file_path)
    if df is not None:
        if chart_type == 'bar':
            plt.bar(df['Quantity'], df['Quantity'], width=0.5, color='red')  # Using Quantity for both axes for illustration
        elif chart_type == 'line':
            plt.plot(df['Quantity'], df['Quantity'], marker='o', linestyle='-', color='red')
        plt.xlabel('Total Units Imported')
        plt.ylabel('Total Units Sold')
        plt.title('Total Units Imported vs Total Units Sold')
        plt.show()

def exit_terminal():
    if os.name == 'nt':  # Windows
        subprocess.call('taskkill /IM cmd.exe /F')
    else:  # Unix or Linux
        subprocess.call('killall -9 terminator', shell=True)  # Replace 'terminator' with your terminal name if needed

def menu():
    while True:
        print()
        print("1. Display Records")
        print("2. Cost Vs MRP (Bar/Line)")
        print("3. Cost Vs Total Goods Sold (Bar/Line)")
        print("4. Total Good Imported Vs Total Goods Sold (Bar/Line)")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_records()
        elif choice == 2:
            chart_type = input("Enter 'bar' or 'line': ")
            cost_vs_mrp(chart_type)
        elif choice == 3:
            chart_type = input("Enter 'bar' or 'line': ")
            cost_vs_total_units_sold(chart_type)
        elif choice == 4:
            chart_type = input("Enter 'bar' or 'line': ")
            total_units_imported_vs_sold(chart_type)
        elif choice == 5:
            print("Exiting...")
            exit_terminal()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Start the menu
menu()