import json
import pprint
import os

FILENAME = 'invoices.json'

# Load existing invoices from file, if any
def load_invoices():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            return json.load(f)
    return []

def save_invoices(invoices):
    with open(FILENAME, 'w') as f:
        json.dump(invoices, f, indent=4)  # indent=4 parameter in Python's json.dump() (and json.dumps()) function specifies that the output JSON should be pretty-printed with an indentation of 4 spaces per level.

def create_invoice():
    invoice = {}
    invoice['invoice_number'] = input("Enter invoice number: ")
    invoice['date'] = input("Enter invoice date (YYYY-MM-DD): ")
    client = {
        'name': input("Enter client name: "),
        'email': input("Enter client email: "),
        'address': input("Enter client address: ")
    }
    invoice['client'] = client
    items = []
    while True:
        desc = input("Item description (or 'done' to finish): ")
        if desc.lower() == 'done':
            break
        qty = int(input("Quantity: "))
        unit_price = float(input("Unit price: "))
        items.append({'description': desc, 'quantity': qty, 'unit_price': unit_price})
    invoice['items'] = items
    
    # calculations
    subtotal = 0                # initialize subtotal
    for item in items:
        subtotal += item['quantity']*item['unit_price']          # add each item's total to subtotal
    invoice['subtotal'] = subtotal
    tax = 0.10 * subtotal
    invoice['tax'] = tax
    invoice['total'] = subtotal + tax
    invoice['status'] = 'draft'
    return invoice

def list_invoices(invoices):
    if not invoices:
        print("No invoices found.")
        return
    for idx, inv in enumerate(invoices, 1):                 # The second argument 1 means the enumeration will start counting from 1 instead of the default 0.
        print(f"{idx}. Invoice #{inv['invoice_number']} | {inv['client']['name']} | Total: {inv['total']} | Status: {inv['status']}")

def view_invoice(invoices):
    idx = int(input("Enter invoice list number to view details (list index): ")) - 1
    if 0 <= idx < len(invoices):                # 0 <= idx ensures the index is not negative and idx < len(invoices) ensures the index is less than the total number of invoices.
        pprint.pprint(invoices[idx])
    else:
        print("Invalid selection.")

def main():
    invoices = load_invoices()
    while True:
        print("\n--- INVOICING SYSTEM ---")
        print("1. Create Invoice")
        print("2. List Invoices")
        print("3. View Invoice")
        print("4. Exit")
        choice = input("Choose an action: ")
        if choice == '1':
            invoice = create_invoice()
            invoices.append(invoice)
            save_invoices(invoices)
            print("Invoice saved!\n")
        elif choice == '2':
            list_invoices(invoices)
        elif choice == '3':
            list_invoices(invoices)
            view_invoice(invoices)
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
