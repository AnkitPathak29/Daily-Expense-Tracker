🧾 Daily Expense Tracker-Readme
-

A Simple CLI-Based Personal Expense Logging Application

📌 Overview
-

The Daily Expense Tracker is a Python-based command-line application that allows users to record, view, summarize, and manage daily expense entries. It is designed as a lightweight and interactive tool for tracking day-to-day spending without requiring databases or external dependencies (other than pandas).

This project demonstrates:

•	Input handling
•	Data validation
•	Modular programming
•	Use of lists & dictionaries
•	Use of pandas for tabular representation
•	File-free in-memory data handling

🎯 Project Objectives
-

This project aligns with the "Build Your Own Project" guidelines by:

•	Identifying a common real-world problem -> keeping track of daily expenses.
•	Designing a CLI system for structured recording of transactions.
•	Implementing the solution using Python concepts like loops, functions, data structures, and error handling.
•	Documenting the workflow, architecture, and functionality clearly.

✨ Features
-

1. Add New Transaction

•	Takes item name, quantity, and price
•	Automatically calculates subtotal
•	Stores with real-time timestamp

2. View Transaction Log

•	Shows all recorded expenses in a clean formatted table
•	Uses pandas for tabular formatting

3. Daily Summary

•	Shows total number of entries
•	Displays grand total expenditure


4. Reset Transaction Log

•	Clears all data to start a new day

5. Exit Application

•	Gracefully closes the program



🛠 Technologies & Tools Used

•	Python 3.12

•	Pandas library (for DataFrame table view)

•	time module (for timestamping entries)

•	CLI-based user interface


📂 Project Structure
-

  *Dailyexpensetracker.py    # Main project file containing all modules
  
  *README.md    # Project documentation

  *Statement.md    # Project statement

🧩 System Architecture (High-Level)
-

User Input
     ↓
Input Validation
     ↓
Transaction Creation
     ↓
Data Processing & Storage (in-memory list)
     ↓
Display (pandas DataFrame & print)

👨‍💻 How to Install & Run
-

1️⃣ Install Python

Ensure Python 3.12 is installed.
Check using:
python 3.12

2️⃣ Install Required Libraries
pip install pandas

3️⃣ Run the Program
python expense_tracker.py

🧪 Testing Instructions
-

1. Test Add Transaction
•	Try valid & invalid inputs: empty name, negative price, non-numeric quantity

2. Test Log Display

•	Add multiple transactions
•	Verify table formatting

3. Test Summary

•	Add items -> compare calculated totals
4. Test Reset Log

•	Enter "yes" and verify empty table
•	Enter "no" → ensure data still exists

5. Boundary Testing

•	Very large numbers
•	Decimal pricing
•	Special characters in item names


🚀 Future Enhancements
-

•	Export log to CSV or Excel

•	Add category-wise expense filtering

•	Add daily/weekly/monthly analytics

•	GUI using Tkinter or Streamlit

•	Persistent storage (SQLite / JSON)


👥 Target Users
-

•	Students

•	Households

•	Small shop owners

•	Anyone wanting a simple text-based expense tracker




📄 License
-

•	This project is open for educational and non-commercial use.

