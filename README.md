# Medicine Inventory Management System

A simple Python-based application to manage medicine inventory for small clinics, medical shops, or college mini-projects.  
This version stores data in memory using Python lists and dictionaries.  
It includes features like adding medicines,viewing inventory,checking low stock,showing expired medicines,and removing medicines

---

## 🔥 Features

### ✔ Add New Medicines
- Stores name,quantity,expiry date
- Automatically capitalizes medicine names
- Prevents adding invalid data

### ✔ View Inventory(Clean Table Format)
- Displays all stored medicines using the tabulate library
- Professional table formatting in the terminal

### ✔ Low Stock Alerts
- Highlights medicines with stock *below 10*

### ✔ Expired Medicines Detection
- Compares expiry date with today’s date
- Shows medicines that are already expired

### ✔ Remove Medicines
- You can remove medicines by entering their name
- Safe removal with "not found" handling

---

## 📁 Project Structure
MEDICINE INVENTORY MANAGEMENT SYSTEM/
|
|-medicine_inventory.py
|-README.md

---

## 🛠 Requirement

You only need:

- Python
- VS Code(or any editor)
- The tabulate library (install using the command below)

Install tabulate:

```bash
pip install tabulate  (write this in terminal)




