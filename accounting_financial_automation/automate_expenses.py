from collections import defaultdict
from datetime import datetime
import json
import os
import pprint


EXPENSE_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

CATEGORIES = [
    "Travel",
    "Office Supplies",
    "Meals & Entertainment",
    "Utilities",
    "Other"
]

def choose_category():
    print("Select a category:")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}. {cat}")
    choice = input(f"Enter category number (1-{len(CATEGORIES)}) :")
    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(CATEGORIES):
            return CATEGORIES[idx-1]
    return choice  # user typed a custom category


def add_expense():
    expense = {}
    expense['date'] = input("Enter expense date (YYYY-MM-DD): ")
    expense['category'] = choose_category()
    expense['description'] = input("Enter expense description: ")
    expense['amount'] = float(input("Enter amount: "))
    return expense

def list_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. {exp['date']} | {exp['category']} | {exp['description']} | Amount: {exp['amount']}")

def report_total_by_category(expenses):
    totals = defaultdict(float)                 # defaultdict(float) means: if you access a key that doesn't exist yet, automatically create it with a default float value of 0.0.
    for exp in expenses:
        totals[exp['category']] += exp['amount']    # it becomes like this: Travel + 1000 and insert it into the default dictionary thus it becomes {Travel:1000}, accumulating as you iterate through the list

    print("\nTotal Spent by Category:")
    print("-" * 30)
    for cat, total in totals.items():           # items() returns key-value pairs as tuples.
        print(f"{cat:20} : ₹{total:.2f}")       # {cat:20} means  gives a minimum width of 20 characters for the printed category string
    print("-" * 30)

def report_total_by_month(expenses):
    month = input("Enter month to filter by (YYYY-MM): ")
    total = 0
    for exp in expenses:
        if exp['date'].startswith(month):
            total += exp['amount']
    print(f"\nTotal expenses for {month}: ₹{total:.2f}")

def main_expense_module():
    expenses = load_expenses()
    while True:
        print("\n--- EXPENSE TRACKING ---")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Report: Total by Category")
        print("4. Report: Total by Month")
        print("5. Exit Expense Module")
        print('\n')
        choice = input("Select an option: ")
        if choice == '1':
            expense = add_expense()
            expenses.append(expense)
            save_expenses(expenses)
            print("Expense saved!")
        elif choice == '2':
            list_expenses(expenses)
        elif choice == '3':
            report_total_by_category(expenses)
        elif choice == '4':
            report_total_by_month(expenses)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_expense_module()
