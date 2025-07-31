
import automate_invoicing
import automate_expenses
import automate_payroll


def auto_accounting():
    while True:
        print("\n=== ACCOUNTING & FINANCIAL AUTOMATION ===")
        print("1. Invoicing")
        print("2. Expense Tracking")
        print("3. Payroll")
        print("4. Exit Program")
        print('\n')
        choice = input("Choose an option: ")
        if choice == '1':
            automate_invoicing.main()
        elif choice == '2':
            automate_expenses.main_expense_module()
        elif choice == '3':
            automate_payroll.payroll_menu()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    auto_accounting()

            
