# Basic structure

invoice1 = {
    'invoice_number': 'INV001',
    'date': '2025-07-31',
    'client': {
        'name': 'ABC Corp',
        'email': 'client@abccorp.com',
        'address': '123 Main St, City, Country'
    },
    'items': [
        {'description': 'Consulting Service', 'quantity': 10, 'unit_price': 50},
        {'description': 'Software License', 'quantity': 2, 'unit_price': 200}
    ],
    'subtotal': 900,  # (10*50 + 2*200)
    'tax': 90,        # Example, 10%
    'total': 990,
    'status': 'sent'
}

expense = {
    'date': '2025-07-31',
    'category': 'Travel',
    'description': 'Taxi fare to client meeting',
    'amount': 30.00
}

employee1 = {
    "id": "E001",
    "name": "John Doe",
    "position": "Software Developer",
    "monthly_salary": 50000,
    "tax_rate": 0.1  # 10% tax
}