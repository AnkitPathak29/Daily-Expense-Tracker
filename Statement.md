Statement.md
-

📌 Problem Statement
-

Managing daily expenses manually often leads to missing entries, calculation mistakes, or difficulty in tracking where money is being spent. Most digital expense apps require installation, registration, or internet access. There is a need for a simple, lightweight, offline, command-line based expense tracker that can record transactions quickly and display real-time summaries without requiring complex setup.

🎯 Scope of the Project
-

The scope of this project includes:
-

•	A command-line interface for entering and viewing expense records.
•	Storing transactions temporarily in memory (list of dictionaries).
•	Handling input validation for quantity, price, and item names.
•	Displaying transaction logs in tabular format using pandas.
•	Providing a daily expenditure summary.
•	Allowing the user to clear all records for a new day.

👥 Target Users
-

This project is suitable for:
-

•	Students managing daily or monthly expenses.
•	Small shopkeepers wanting a quick billing log.
•	Homemakers keeping track of grocery spending.
•	Anyone preferring a lightweight and offline expense-tracking system.

🔧 High-Level Features
-

1. Add New Expense Entry

•	Accepts product/service name.
•	Accepts quantity and price.
•	Computes subtotal automatically.
•	Auto-generates timestamp.
•	Performs input validation.

2. View Transaction Log

•	Displays all recorded expenses in a formatted pandas table
•	Shows item name, quantity, price, subtotal, and time

3. View Daily Summary

•	Shows total number of transactions recorded
•	Computes grand total of the day’s expenditure

4. Clear All Transactions

•	Resets the entire log after confirmation
•	Useful for starting a fresh daily expense cycle

5. User-Friendly Command Line Menu

•	Simple menu-based navigation
•	Error-handling for invalid choices
