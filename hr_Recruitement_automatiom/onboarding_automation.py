# Mark applicant as “Hired” and convert to employee
def hire_applicant(applicants, employees, applicant_id):
    for i, applicant in enumerate(applicants):
        
        if applicant["id"] == applicant_id:
            applicant["status"] = "Hired"                       # # Update applicant status
            
            new_employee_id = len(employees) + 101              # Create employee record
            employee = {
                "id": new_employee_id,
                "name": applicant["name"],
                "email": applicant["email"],
                "position": applicant["position_applied"],
                "onboarded": False,
                
                "onboarding_tasks": {
                    "Signed Contract": False,
                    "Completed Tax Forms": False,
                    "Attended Orientation": False,
                    "Set up Workstation": False
                },
                "documents_received": {
                    "Contract": False,
                    "ID Proof": False,
                    "Certificates": False}
            }
            employees.append(employee)
            
            print(f"{applicant['name']} hired! Employee record created with onboarding checklist.")
            del applicants[i]                                   # remove from applicants list if you like
            
            return
    print(f"Applicant ID {applicant_id} not found or already hired.")

# Complete onboarding
def complete_onboarding_task(employees, employee_id, task):
    for employee in employees:
        if employee["id"] == employee_id:
            if task in employee["onboarding_tasks"]:
                employee["onboarding_tasks"][task] = True
                print(f"Task '{task}' marked as complete for employee {employee['name']}.")
            else:
                print(f"Task '{task}' not found.")
            return
    print(f"Employee ID {employee_id} not found.")

# recieve document
def receive_document(employees, employee_id, document):
    for employee in employees:
        if employee["id"] == employee_id:
            if document in employee["documents_received"]:
                employee["documents_received"][document] = True
                print(f"Document '{document}' received for employee {employee['name']}.")
            else:
                print(f"Document '{document}' not tracked.")
            return
    print(f"Employee ID {employee_id} not found.")

# Function to Check Onboarding task Progress
def check_onboarding_status(employees, employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            print(f"Onboarding status for {employee['name']}:")
            print("Tasks:")
            
            for task, done in employee["onboarding_tasks"].items():             # items() is a method used with dictionaries. It returns a view object that displays a list of the dictionary’s key-value pairs as tuples.
                if done:
                    status = "Done"
                else:
                    status = "Pending"
                print(f"Onboard {task} is {status}")
            
            print("Documents:")
           
            for doc, received in employee["documents_received"].items():
                print(f"  {doc}: {'Received' if received else 'Missing'}")
            return
    print(f"Employee ID {employee_id} not found.")
