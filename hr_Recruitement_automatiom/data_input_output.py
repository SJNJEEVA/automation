# we are goinge to store the information as individual dictionaries  and these dictionaries are collected inside one list per data type. 
    # This keeps all related entries organized and easy to manage in memory.

# 1.Add Applicants
applicants = [] 

def add_applicant(applicants, name, email, position_applied):
    new_id = len(applicants) + 1  # Adding + 1 means you are assigning a new ID that is one more than the current count of applicants.
    applicant = {
        "id": new_id,
        "name": name,
        "email": email,
        "position_applied": position_applied,
        "status": "Applied"
    }
    applicants.append(applicant)
    print(f"Applicant {name} added with ID {new_id} and applied for{position_applied}")

# 2.Add Employees
employees = []  

def add_employee(employees, name, email, position):
    new_id = len(employees) + 10  # Employee IDs start from 101
    employee = {
        "id": new_id,
        "name": name,
        "email": email,
        "position": position,
        "onboarded": False
    }
    employees.append(employee)
    print(f"Employee {name} added with ID {new_id}")







