import time
import pandas as pd
import os

TRANSACTIONS = []

def record_transaction():
    print("\n---New Expense Entry---")
    
    #Asking for Product/Service Name.
    item_name=input("Enter the name of product bought/Servive utilised: ").strip()  
    if not item_name:
        print("Error: It cannot be empty.")
        return

    #Get Quantity
    while True:
        try:
            quantity_str=input("Enter the Quantity/number : ")
            qty=int(quantity_str)
            if qty <= 0:
                print("Error: Quantity must be a positive integer.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a whole number for quantity.")

    #Get Price
    while True:
        try:
            price_str=input("Enter Unit Price (₹): ")
            prc=float(price_str)
            if prc <= 0:
                print("Error: Price must be greater than zero.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a number for the price (e.g., 2).")

    #Calculate subtotal
    subtotal=qty * prc
    current_time=time.strftime("%H:%M:%S")

    #Create and store the new transaction record
    new_record={"Time": current_time,"Item Name": item_name,"Quantity": qty,"Price": prc,"Subtotal": subtotal}
    
    #Add to the beginning of the list (newest first)
    TRANSACTIONS.insert(0, new_record) 
    
    print(f"\n Transaction Recorded: {item_name} x{qty} @ ₹{prc:.2f} = ₹{subtotal:.2f}")

def display_log():
    """Displays the entire transaction history in a formatted table."""
    if not TRANSACTIONS:
        print("\n---TransactionLog ---")
        print("No transactions recorded yet.")
        return

    print("\n---Transaction Log---")
    
    #Convert list of dicts to DataFrame.
    df = pd.DataFrame(TRANSACTIONS)
    
    #Format currency columns for display.
    df['Price']=df['Price'].apply(lambda x: f"₹{x:.2f}")
    df['Subtotal']=df['Subtotal'].apply(lambda x: f"₹{x:.2f}")

    #Display the table using pandas string representation.
    print(df.to_string(index=False, col_space=12))
    print("-" * 75)
    
def calculate_summary():
    """Calculates and displays the total sales for the day."""
    total_sales=len(TRANSACTIONS)
    grand_total=sum(t["Subtotal"] for t in TRANSACTIONS)
    
    print("\n--- Daily Sales Summary ---")
    print(f"Total Items Logged: {total_sales}")
    print(f"Grand Total Sales: ₹{grand_total:,.2f}")
    print("-" * 30)

def reset_log():
    """Clears all transactions."""
    global TRANSACTIONS
    confirm=input("Are you sure you want to clear all transactions? (yes/no): ").lower().strip()
    if confirm=='yes':
        TRANSACTIONS = []
        print("All transactions cleared. Starting a new day.")
    else:
        print("Operation cancelled.")

def main():
    """Main application loop."""
    print("==========================================")
    print("Daily Expense Tracker")
    print("==========================================")
    
    while True:
        print("\n---Expense---")
        print("1: Add New Name of Product/Service")
        print("2: View Transaction Log")
        print("3: View Daily Summary")
        print("4: Clear All Transactions (Start New Day)")
        print("5: Exit Program")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            record_transaction()
        elif choice == '2':
            display_log()
        elif choice == '3':
            calculate_summary()
        elif choice == '4':
            reset_log()
        elif choice == '5':
            print("\nThank you for using Daily Expense Tracker,GoodBye!")
            break
        else:
            print("\nError: Invalid choice. Please select a number between 1 and 5.")
        
        #Pause before showing the menu again
        input("\nPress Enter to continue...")

#The pandas DataFrame is necessary here for tabular output in the console.
if __name__ == "__main__":
    main()
    
