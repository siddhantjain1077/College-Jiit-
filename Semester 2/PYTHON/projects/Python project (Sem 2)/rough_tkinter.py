import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import os
import subprocess

#import 

# Set options to display all rows and columns
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

df = None  # Global variable to store DataFrame


def import_csv_file():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path)
            print("CSV file imported successfully.")
            menu()  # Call the menu function after loading the file
        except Exception as e:
            print(f"Error: {e}")

def display_records():
    global df
    if df is not None:
        print(df)
    else:
        print("No DataFrame loaded.")


def cost_vs_mrp(chart_type="bar"):
    global df
    if df is not None:
        if chart_type == "bar":
            plt.bar(df["Total"], df["cogs"], width=0.5, color="blue")
            plt.xlabel("Total")
            plt.ylabel("Cost Price")
            plt.title("Cost vs MRP (Bar Chart)")
            plt.show()
        elif chart_type == "line":
            plt.plot(df["Total"], df["cogs"], marker="o", linestyle="-", color="blue")
            plt.xlabel("Total")
            plt.ylabel("Cost Price")
            plt.title("Cost vs MRP (Line Chart)")
            plt.show()
        elif chart_type == "hist":
            plt.hist(df["Total"], bins=20, color="red")
            plt.xlabel("Total")
            plt.ylabel("Frequency")
            plt.title("Histogram of Total")
            plt.show()
        else:
            print("Invalid chart type. Please choose 'bar', 'line', or 'hist'.")
    else:
        print("No DataFrame loaded.")


def cost_vs_total_units_sold(chart_type="bar"):
    global df
    if df is not None:
        if chart_type == "bar":
            plt.bar(df["Quantity"], df["cogs"], width=0.5, color="green")
            plt.xlabel("Total Units Sold")
            plt.ylabel("Cost Price")
            plt.title("Cost vs Total Units Sold (Bar Chart)")
            plt.show()
        elif chart_type == "line":
            plt.plot(df["Quantity"], df["cogs"], marker="o", linestyle="-", color="green")
            plt.xlabel("Total Units Sold")
            plt.ylabel("Cost Price")
            plt.title("Cost vs Total Units Sold (Line Chart)")
            plt.show()
        elif chart_type == "hist":
            plt.hist(df["Quantity"], bins=20, color="orange")
            plt.xlabel("Total Units Sold")
            plt.ylabel("Frequency")
            plt.title("Histogram of Total Units Sold")
            plt.show()
        else:
            print("Invalid chart type. Please choose 'bar', 'line', or 'hist'.")
    else:
        print("No DataFrame loaded.")


def total_units_imported_vs_sold(chart_type="line"):
    global df
    if df is not None:
        if chart_type == "bar":
            plt.bar(df["Quantity"], df["Quantity"], width=0.5, color="red")
            plt.xlabel("Total Units Imported")
            plt.ylabel("Total Units Sold")
            plt.title("Total Units Imported vs Total Units Sold (Bar Chart)")
            plt.show()
        elif chart_type == "line":
            plt.plot(df["Quantity"], df["Quantity"], marker="o", linestyle="-", color="red")
            plt.xlabel("Total Units Imported")
            plt.ylabel("Total Units Sold")
            plt.title("Total Units Imported vs Total Units Sold (Line Chart)")
            plt.show()
        elif chart_type == "hist":
            plt.hist(df["Quantity"], bins=20, color="purple")
            plt.xlabel("Total Units Imported")
            plt.ylabel("Total Units Sold")
            plt.title("Histogram of Total Units Imported vs Total Units Sold")
            plt.show()
        else:
            print("Invalid chart type. Please choose 'bar', 'line', or 'hist'.")
    else:
        print("No DataFrame loaded.")


def exit_terminal():
    
    os.system("taskkill /F /IM code.exe")
    sys.exit(0)

def menu():
    while True:
        print()
        print("1. Display Records")
        print("2. Cost Vs MRP (Bar/Line/hist)")
        print("3. Cost Vs Total Goods Sold (Bar/Line/hist)")
        print("4. Total Good Imported Vs Total Goods Sold (Bar/Line/hist)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_records()
        elif choice == "2":
            chart_type = input("Enter 'bar', 'line', or 'hist': ")
            cost_vs_mrp(chart_type)
        elif choice == "3":
            chart_type = input("Enter 'bar', 'line', or 'hist': ")
            cost_vs_total_units_sold(chart_type)
        elif choice == "4":
            chart_type = input("Enter 'bar', 'line', or 'hist': ")
            total_units_imported_vs_sold(chart_type)
        elif choice == "5":
            print("Exiting...")
            exit_terminal()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Create a tkinter window
window = tk.Tk()
window.title("CSV File Importer")

# Create an "Add File" button
add_file_button = tk.Button(window, text="Add File", command=import_csv_file)
add_file_button.pack()

# Run the tkinter event loop
window.mainloop()

menu()