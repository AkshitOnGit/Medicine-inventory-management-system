# Project Title

Medicine Inventory Management System

# Overview of the Project

The Medicine Inventory Management System is a Python-based application designed to help clinics, pharmacies, and students maintain an organized record of medicines.
The system allows users to add, view, update, and monitor medicines along with their quantity and expiry dates.
It is a menu-driven console program built for simplicity, accuracy, and learning core programming concepts.

This project was developed to demonstrate:
	•	Inventory handling using Python lists and dictionaries
	•	Basic input validation
	•	Date comparison using the datetime module
	•	A clean, user-friendly command-line interface

⸻

# Features

1. Add Medicine
	•	Stores name, quantity, and expiry date
	•	Validates inputs
	•	Avoids duplicate entries

2. View Inventory
	•	Displays all medicines in a neat table format
	•	Shows name, quantity, and expiry

3. Check Low Stock
	•	Highlights medicines with quantity below a predefined limit
	•	Helps in timely restocking

4. Show Expired Medicines
	•	Compares expiry date with the current date
	•	Lists medicines that are past their expiry

5. Remove Medicine
	•	Allows deletion of discontinued or outdated medicines
	•	Handles cases where the medicine may not exist

6. Menu-Driven User Interface
	•	Easy navigation
	•	Clear instructions
	•	Runs until user chooses to exit

⸻

# Technologies / Tools Used
	•	Python 3.x
	•	VS Code / PyCharm (optional, any IDE works)
	•	tabulate (Python library) for formatted table output
	•	datetime module for date comparison

# Steps to Install and Run the Project

1. Install Python

Download Python 3.x from the official website or verify installation using "python --version" in the terminal.

2. Install Required Library

Install the tabulate library using "pip install tabulate" in the terminal.

3. Download or Create Project File

Make a file named "inventory.py" paste the complete prject code into it.

4. Run the program

Navigate to the folder in termianl and run "python inventory,py",the menu will appear,and you can start using the system.

# Instructions for Testing the Project

To test the system:

1. Add Sample Medicines

Try adding:
	•	Valid medicines
	•	Duplicate names
	•	Invalid dates
	•	Invalid quantities

Check if validations work.

2. View Inventory

Ensure the table shows all medicines clearly.

3. Test Low Stock Function

Add a medicine with quantity < 5
Check if it appears in the low stock list.

4. Test Expiry Feature

Add one past-date medicine, for example 01/01/2023,ensure it appears in the expired medicines list.
