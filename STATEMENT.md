# Problem Statement

Managing medicines manually often leads to several issues such as misplaced records, forgotten expiry dates, inaccurate stock tracking, and difficulty identifying low-quantity items. These challenges can result in wastage, inefficiency, and potential health risks.
To overcome these drawbacks, there is a need for a structured and reliable system that stores medicine information, updates stock accurately, checks expiry dates, and provides quick retrieval of important data.


# Scope of the Project

The scope of this project is limited to the creation of a menu-driven, console-based Medicine Inventory Management System. The system focuses on basic yet essential medicine management operations, including:

	•	Maintaining an internal database of medicines using Python dictionaries.
	•	Storing key details such as medicine name, quantity, and expiry date.
	•	Allowing users to add, view, and remove medicines in a streamlined manner.
	•	Identifying medicines that are low in stock (≤ 5).
	•	Detecting expired medicines by comparing stored dates with the current system date.
	•	Presenting inventory data using structured table formatting for readability.

This system is designed to be simple, lightweight, and suitable for small-scale use and academic demonstration.


# Target Users

This project is intended for the following user groups:

1. Students

Those learning basic Python programming concepts such as dictionaries, functions, modular code, and user interaction.

2. Small Clinics or Local Medical Stores

Where staff may require a basic and efficient tool to track medicines without installing heavy software or databases.

3. Home Users

Individuals who want to monitor their personal medicine stocks, expiry dates, and availability.

4. Academic Institutions

Teachers or evaluators who require a demonstration of applied programming concepts in a practical project.


# High-Level Features

The system includes the following core functionalities:

✔ 1. Add Medicine

Allows users to store new medicine entries with quantity and expiry date.

✔ 2. View Inventory

Displays all stored medicines in a neat, tabulated format using the tabulate library for clarity.

✔ 3. Low Stock Detection

Identifies medicines with quantity less than or equal to five, helping users restock on time.

✔ 4. Expiry Check

Automatically compares expiry dates with today’s date and lists all expired medicines.

✔ 5. Medicine Removal

Provides controlled removal of medicines with confirmation to avoid accidental deletions.

✔ 6. User-Friendly Navigation

A simple and intuitive menu-driven interface makes the system easy to operate for all user categories.