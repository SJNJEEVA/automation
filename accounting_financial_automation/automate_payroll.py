import json
import os

EMPLOYEE_FILE = 'employees.json'
PAYROLL_FILE = 'payslips.json'

# ---------- Helper Functions for File Storage ----------

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# ---------- Employee Management ----------

def add_employee():
    emp = {}
    emp['id'] = input("Enter employee ID: ")
    emp['name'] = input("Enter name: ")
    emp['position'] = input("Enter position/role: ")
    emp['monthly_salary'] = float(input("Enter monthly salary: "))
    emp['tax_rate'] = float(input("Enter tax rate (e.g., 0.1 for 10%): "))
    return emp

def list_employees(employees):
    if not employees:
        print("No employees found.")
        return
    print("\nEmployee List:")
    print("-" * 50)
    for idx, emp in enumerate(employees, 1):
        print(f"{idx}. {emp['id']} | {emp['name']} | {emp['position']} | Salary: ₹{emp['monthly_salary']} | Tax Rate: {emp['tax_rate']*100}%")
    print("-" * 50)

# ---------- Payroll Processing ----------

def process_payroll(employees):
    payslips = []
    for emp in employees:
        gross = emp['monthly_salary']
        tax = gross * emp['tax_rate']
        net = gross - tax
        payslip = {
            'employee_id': emp['id'],
            'name': emp['name'],
            'position': emp['position'],
            'gross_pay': gross,
            'tax': tax,
            'net_pay': net
        }
        payslips.append(payslip)
    return payslips

def list_payslips(payslips):
    if not payslips:
        print("No payslips found.")
        return
    print("\nPayroll for Employees:")
    print("-" * 60)
    for ps in payslips:
        print(f"{ps['employee_id']} | {ps['name']} | {ps['position']} | Gross: ₹{ps['gross_pay']} | Tax: ₹{ps['tax']} | Net: ₹{ps['net_pay']}")
    print("-" * 60)

def display_payslip(payslips):
    emp_id = input("Enter employee ID to view payslip: ")
    found = False
    for ps in payslips:
        if ps['employee_id'] == emp_id:
            found = True
            print("\n--- Payslip ---")
            print(f"Employee ID: {ps['employee_id']}")
            print(f"Name      : {ps['name']}")
            print(f"Position  : {ps['position']}")
            print(f"Gross Pay : ₹{ps['gross_pay']:.2f}")
            print(f"Tax       : ₹{ps['tax']:.2f}")
            print(f"Net Pay   : ₹{ps['net_pay']:.2f}")
            print("--------------")
            break
    if not found:
        print("Payslip not found for that employee ID.")

# ---------- Main Menu ----------

def payroll_menu():
    employees = load_data(EMPLOYEE_FILE)
    payslips = load_data(PAYROLL_FILE)

    while True:
        print("\n--- PAYROLL MODULE ---")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Process Payroll (Calculate Payslips)")
        print("4. List All Payslips")
        print("5. View Payslip by Employee ID")
        print("6. Exit Payroll Module")
        choice = input("Select an option: ")

        if choice == '1':
            emp = add_employee()
            employees.append(emp)
            save_data(employees, EMPLOYEE_FILE)
            print("Employee added.")

        elif choice == '2':
            list_employees(employees)

        elif choice == '3':
            payslips = process_payroll(employees)
            save_data(payslips, PAYROLL_FILE)
            print("Payroll processed and payslips saved.")

        elif choice == '4':
            list_payslips(payslips)

        elif choice == '5':
            display_payslip(payslips)

        elif choice == '6':
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    payroll_menu()
