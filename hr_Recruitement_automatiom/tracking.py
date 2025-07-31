# Find and Display Applicants by name
def find_applicant_by_name(applicants, search_name):
    results = []
    for applicant in applicants:
        name_lower = applicant["name"].lower()              # Convert applicant name and search term to lowercase for case-insensitive comparison
        search_lower = search_name.lower()
    
        if search_lower in name_lower:                      # Check if the search term is inside the applicant's name
            results.append(applicant)
    
    if results:
        for applicant in results:
            print(applicant)
    else:
        print(f"No applicants found with name containing '{search_name}'.")

# Find and Display Applicants by id
def find_applicant_by_id(applicants, applicant_id):
    for applicant in applicants:
        if applicant["id"] == applicant_id:
            print(applicant)
            return applicant
    print(f"Applicant ID {applicant_id} not found.")
    return None

# Remove Applicants or Employees
def remove_applicant(applicants, applicant_id):
    for i, applicant in enumerate(applicants):
        if applicant["id"] == applicant_id:
            del applicants[i]
            print(f"Applicant ID {applicant_id} removed.")
            return
    print(f"Applicant ID {applicant_id} not found.")

# Mark Employee Onboarded
def mark_employee_onboarded(employees, employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            employee["onboarded"] = True
            print(f"Employee ID {employee_id} marked as onboarded.")
            return
    print(f"Employee ID {employee_id} not found.")



def list_all_applicants(applicants):
    if not applicants:
        print("No applicants in the system.")
    for applicant in applicants:
        print(applicant)