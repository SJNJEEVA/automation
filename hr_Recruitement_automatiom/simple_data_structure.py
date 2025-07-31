# List to store multiple applicants
applicants = []                             # Applicants: Track who applied, contact info, which job, and their current recruitment status.

# Example applicant entry
applicant = {
    "id": 1,  # unique applicant ID
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "position_applied": "Software Engineer",
    "status": "Interview Scheduled"  # could also be "Applied", "Hired", etc.
}

# List to store employees
employees = []                              # Employees: Store key staff details, position, and whether they’ve completed onboarding.

# Example employee entry
employee = {
    "id": 101,  # unique employee ID
    "name": "John Smith",
    "email": "john@example.com",
    "position": "HR Manager",
    "onboarded": True  # True if onboarding complete, False otherwise
}

# List to store shift schedules
schedules = []                              # Schedules: Link employees to specific work dates and shift times.

# Example schedule entry
schedule = {
    "employee_id": 101,
    "date": "2025-08-01",  # YYYY-MM-DD format
    "shift": "09:00-17:00"
}
