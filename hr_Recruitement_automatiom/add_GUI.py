import tkinter as tk
from tkinter import messagebox, ttk
import re
from datetime import datetime, timedelta

employees = []
schedules = []

class HrAutoGui:
    def __init__(self, root):
        self.root = root
        self.root.title("HR Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")

        self.applicants = []
        self.employees = employees
        self.schedules = schedules

        # Create main frame
        self.main_frame = tk.Frame(root, bg="lightblue")
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Center frame for buttons
        self.button_frame = tk.Frame(self.main_frame, bg="lightblue")
        self.button_frame.pack(anchor="center", pady=20)

        # Bottom frame for output and input fields
        self.bottom_frame = tk.Frame(self.main_frame, bg="lightblue")
        self.bottom_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        # Output text area (smaller, rectangular)
        self.output_text = tk.Text(self.bottom_frame, height=5, width=60)
        self.output_text.pack(pady=5)
        self.output_text.config(state="disabled")

        # Input frame below output
        self.input_frame = tk.Frame(self.bottom_frame, bg="lightblue")
        self.input_frame.pack(fill="x", padx=10)

        # Input fields dictionary
        self.entries = {}
        self.current_action = None

        # Create buttons for each action
        self.create_buttons()

    def create_buttons(self):
        actions = [
            ("Add Applicant", self.show_add_applicant),
            ("Add Employee", self.show_add_employee),
            ("Find Applicant by Name", self.show_find_applicant_name),
            ("Find Applicant by ID", self.show_find_applicant_id),
            ("Remove Applicant", self.show_remove_applicant),
            ("Mark Employee Onboarded", self.show_mark_employee_onboarded),
            ("List All Applicants", self.show_list_all_applicants),
            ("List All Employees", self.show_list_all_employees),
            ("Hire Applicant", self.show_hire_applicant),
            ("Complete Onboarding Task", self.show_complete_onboarding_task),
            ("Receive Employee Document", self.show_receive_document),
            ("Check Onboarding Status", self.show_check_onboarding_status),
            ("Add Schedule", self.show_add_schedule),
            ("View Schedules by Employee", self.show_view_schedules_employee),
            ("View Schedules by Date", self.show_view_schedules_date),
            ("Update Schedule", self.show_update_schedule),
            ("Remove Schedule", self.show_remove_schedule)
        ]
        for i, (text, command) in enumerate(actions):
            row = i // 4  # 4 buttons per row
            col = i % 4
            tk.Button(self.button_frame, text=text, command=command, width=20).grid(row=row, column=col, padx=5, pady=5)

    def clear_input_frame(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.entries = {}

    def clear_entry_fields(self):
        for entry in self.entries.values():
            if isinstance(entry, tk.Entry):
                entry.delete(0, tk.END)
            elif isinstance(entry, ttk.Combobox):
                entry.set("")

    def display_output(self, message):
        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, message)
        self.output_text.config(state="disabled")

    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))

    def validate_shift(self, shift):
        pattern = r"^\d{2}:\d{2}-\d{2}:\d{2}$"
        if not re.match(pattern, shift):
            return False
        start, end = shift.split("-")
        try:
            start_time = datetime.strptime(start, "%H:%M")
            end_time = datetime.strptime(end, "%H:%M")
            return True
        except ValueError:
            return False

    def show_add_applicant(self):
        self.current_action = "add_applicant"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Name:", bg="lightblue").pack()
        self.entries["name"] = tk.Entry(self.input_frame, width=50)
        self.entries["name"].pack()
        tk.Label(self.input_frame, text="Email:", bg="lightblue").pack()
        self.entries["email"] = tk.Entry(self.input_frame, width=50)
        self.entries["email"].pack()
        tk.Label(self.input_frame, text="Position Applied:", bg="lightblue").pack()
        self.entries["position"] = tk.Entry(self.input_frame, width=50)
        self.entries["position"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_add_employee(self):
        self.current_action = "add_employee"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Name:", bg="lightblue").pack()
        self.entries["name"] = tk.Entry(self.input_frame, width=50)
        self.entries["name"].pack()
        tk.Label(self.input_frame, text="Email:", bg="lightblue").pack()
        self.entries["email"] = tk.Entry(self.input_frame, width=50)
        self.entries["email"].pack()
        tk.Label(self.input_frame, text="Position:", bg="lightblue").pack()
        self.entries["position"] = tk.Entry(self.input_frame, width=50)
        self.entries["position"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_find_applicant_name(self):
        self.current_action = "find_applicant_name"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Search Name:", bg="lightblue").pack()
        self.entries["search_name"] = tk.Entry(self.input_frame, width=50)
        self.entries["search_name"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_find_applicant_id(self):
        self.current_action = "find_applicant_id"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Applicant ID:", bg="lightblue").pack()
        self.entries["applicant_id"] = tk.Entry(self.input_frame, width=50)
        self.entries["applicant_id"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_remove_applicant(self):
        self.current_action = "remove_applicant"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Applicant ID:", bg="lightblue").pack()
        self.entries["applicant_id"] = tk.Entry(self.input_frame, width=50)
        self.entries["applicant_id"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_mark_employee_onboarded(self):
        self.current_action = "mark_employee_onboarded"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Employee ID:", bg="lightblue").pack()
        self.entries["employee_id"] = tk.Entry(self.input_frame, width=50)
        self.entries["employee_id"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_list_all_applicants(self):
        self.current_action = "list_all_applicants"
        self.execute_action()

    def show_list_all_employees(self):
        self.current_action = "list_all_employees"
        self.execute_action()

    def show_hire_applicant(self):
        self.current_action = "hire_applicant"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Applicant ID:", bg="lightblue").pack()
        self.entries["applicant_id"] = tk.Entry(self.input_frame, width=50)
        self.entries["applicant_id"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_complete_onboarding_task(self):
        self.current_action = "complete_onboarding_task"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Employee ID:", bg="lightblue").pack()
        self.entries["employee_id"] = tk.Entry(self.input_frame, width=50)
        self.entries["employee_id"].pack()
        tk.Label(self.input_frame, text="Task:", bg="lightblue").pack()
        self.entries["task"] = ttk.Combobox(self.input_frame, values=[
            "Signed Contract", "Completed Tax Forms", "Attended Orientation", "Set up Workstation"])
        self.entries["task"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_receive_document(self):
        self.current_action = "receive_document"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Employee ID:", bg="lightblue").pack()
        self.entries["employee_id"] = tk.Entry(self.input_frame, width=50)
        self.entries["employee_id"].pack()
        tk.Label(self.input_frame, text="Document:", bg="lightblue").pack()
        self.entries["document"] = ttk.Combobox(self.input_frame, values=["Contract", "ID Proof", "Certificates"])
        self.entries["document"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_check_onboarding_status(self):
        self.current_action = "check_onboarding_status"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Employee ID:", bg="lightblue").pack()
        self.entries["employee_id"] = tk.Entry(self.input_frame, width=50)
        self.entries["employee_id"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_add_schedule(self):
        self.current_action = "add_schedule"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Employee ID:", bg="lightblue").pack()
        self.entries["employee_id"] = tk.Entry(self.input_frame, width=50)
        self.entries["employee_id"].pack()
        tk.Label(self.input_frame, text="Date (YYYY-MM-DD):", bg="lightblue").pack()
        self.entries["date"] = tk.Entry(self.input_frame, width=50)
        self.entries["date"].pack()
        tk.Label(self.input_frame, text="Shift (HH:MM-HH:MM):", bg="lightblue").pack()
        self.entries["shift"] = tk.Entry(self.input_frame, width=50)
        self.entries["shift"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_view_schedules_employee(self):
        self.current_action = "view_schedules_employee"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Employee ID:", bg="lightblue").pack()
        self.entries["employee_id"] = tk.Entry(self.input_frame, width=50)
        self.entries["employee_id"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_view_schedules_date(self):
        self.current_action = "view_schedules_date"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Date (YYYY-MM-DD):", bg="lightblue").pack()
        self.entries["date"] = tk.Entry(self.input_frame, width=50)
        self.entries["date"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_update_schedule(self):
        self.current_action = "update_schedule"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Employee ID:", bg="lightblue").pack()
        self.entries["employee_id"] = tk.Entry(self.input_frame, width=50)
        self.entries["employee_id"].pack()
        tk.Label(self.input_frame, text="Date (YYYY-MM-DD):", bg="lightblue").pack()
        self.entries["date"] = tk.Entry(self.input_frame, width=50)
        self.entries["date"].pack()
        tk.Label(self.input_frame, text="New Shift (HH:MM-HH:MM):", bg="lightblue").pack()
        self.entries["new_shift"] = tk.Entry(self.input_frame, width=50)
        self.entries["new_shift"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def show_remove_schedule(self):
        self.current_action = "remove_schedule"
        self.clear_input_frame()
        tk.Label(self.input_frame, text="Employee ID:", bg="lightblue").pack()
        self.entries["employee_id"] = tk.Entry(self.input_frame, width=50)
        self.entries["employee_id"].pack()
        tk.Label(self.input_frame, text="Date (YYYY-MM-DD):", bg="lightblue").pack()
        self.entries["date"] = tk.Entry(self.input_frame, width=50)
        self.entries["date"].pack()
        tk.Button(self.input_frame, text="Submit", command=self.execute_action).pack(pady=5)

    def execute_action(self):
        try:
            if self.current_action == "add_applicant":
                name = self.entries["name"].get().strip()
                email = self.entries["email"].get().strip()
                position = self.entries["position"].get().strip()
                if not name or not email or not position:
                    messagebox.showerror("Error", "All fields are required.")
                    return
                if not self.validate_email(email):
                    messagebox.showerror("Error", "Invalid email format.")
                    return
                result = self.add_applicant(self.applicants, name, email, position)
                self.display_output(result)
                self.clear_entry_fields()
            elif self.current_action == "add_employee":
                name = self.entries["name"].get().strip()
                email = self.entries["email"].get().strip()
                position = self.entries["position"].get().strip()
                if not name or not email or not position:
                    messagebox.showerror("Error", "All fields are required.")
                    return
                if not self.validate_email(email):
                    messagebox.showerror("Error", "Invalid email format.")
                    return
                result = self.add_employee(self.employees, name, email, position)
                self.display_output(result)
                self.clear_entry_fields()
            elif self.current_action == "find_applicant_name":
                search_name = self.entries["search_name"].get().strip()
                if not search_name:
                    messagebox.showerror("Error", "Search name is required.")
                    return
                result = self.find_applicant_by_name(self.applicants, search_name)
                self.display_output(result)
                self.clear_entry_fields()
            elif self.current_action == "find_applicant_id":
                applicant_id = self.entries["applicant_id"].get().strip()
                if not applicant_id.isdigit():
                    messagebox.showerror("Error", "Applicant ID must be a number.")
                    return
                applicant_id = int(applicant_id)
                result = self.find_applicant_by_id(self.applicants, applicant_id)
                self.display_output(result if result else f"Applicant ID {applicant_id} not found.")
                self.clear_entry_fields()
            elif self.current_action == "remove_applicant":
                applicant_id = self.entries["applicant_id"].get().strip()
                if not applicant_id.isdigit():
                    messagebox.showerror("Error", "Applicant ID must be a number.")
                    return
                applicant_id = int(applicant_id)
                result = self.remove_applicant(self.applicants, applicant_id)
                self.display_output(f"Applicant ID {applicant_id} removed." if result else f"Applicant ID {applicant_id} not found.")
                self.clear_entry_fields()
            elif self.current_action == "mark_employee_onboarded":
                employee_id = self.entries["employee_id"].get().strip()
                if not employee_id.isdigit():
                    messagebox.showerror("Error", "Employee ID must be a number.")
                    return
                employee_id = int(employee_id)
                result = self.mark_employee_onboarded(self.employees, employee_id)
                self.display_output(f"Employee ID {employee_id} marked as onboarded." if result else f"Employee ID {employee_id} not found.")
                self.clear_entry_fields()
            elif self.current_action == "list_all_applicants":
                result = self.list_all_applicants(self.applicants)
                self.display_output(result)
            elif self.current_action == "list_all_employees":
                result = self.list_all_employees(self.employees)
                self.display_output(result)
            elif self.current_action == "hire_applicant":
                applicant_id = self.entries["applicant_id"].get().strip()
                if not applicant_id.isdigit():
                    messagebox.showerror("Error", "Applicant ID must be a number.")
                    return
                applicant_id = int(applicant_id)
                result = self.hire_applicant(self.applicants, self.employees, applicant_id)
                self.display_output(f"Applicant ID {applicant_id} hired and moved to employees." if result else f"Applicant ID {applicant_id} not found or already hired.")
                self.clear_entry_fields()
            elif self.current_action == "complete_onboarding_task":
                employee_id = self.entries["employee_id"].get().strip()
                task = self.entries["task"].get()
                if not employee_id.isdigit():
                    messagebox.showerror("Error", "Employee ID must be a number.")
                    return
                if not task:
                    messagebox.showerror("Error", "Task selection is required.")
                    return
                employee_id = int(employee_id)
                result = self.complete_onboarding_task(self.employees, employee_id, task)
                self.display_output(f"Task '{task}' marked as complete for employee ID {employee_id}." if result else f"Employee ID {employee_id} not found or task '{task}' not valid.")
                self.clear_entry_fields()
            elif self.current_action == "receive_document":
                employee_id = self.entries["employee_id"].get().strip()
                document = self.entries["document"].get()
                if not employee_id.isdigit():
                    messagebox.showerror("Error", "Employee ID must be a number.")
                    return
                if not document:
                    messagebox.showerror("Error", "Document selection is required.")
                    return
                employee_id = int(employee_id)
                result = self.receive_document(self.employees, employee_id, document)
                self.display_output(f"Document '{document}' received for employee ID {employee_id}." if result else f"Employee ID {employee_id} not found or document '{document}' not valid.")
                self.clear_entry_fields()
            elif self.current_action == "check_onboarding_status":
                employee_id = self.entries["employee_id"].get().strip()
                if not employee_id.isdigit():
                    messagebox.showerror("Error", "Employee ID must be a number.")
                    return
                employee_id = int(employee_id)
                result = self.check_onboarding_status(self.employees, employee_id)
                self.display_output(result)
                self.clear_entry_fields()
            elif self.current_action == "add_schedule":
                employee_id = self.entries["employee_id"].get().strip()
                date = self.entries["date"].get().strip()
                shift = self.entries["shift"].get().strip()
                if not employee_id.isdigit():
                    messagebox.showerror("Error", "Employee ID must be a number.")
                    return
                if not re.match(r"\d{4}-\d{2}-\d{2}", date):
                    messagebox.showerror("Error", "Date must be in YYYY-MM-DD format.")
                    return
                if not self.validate_shift(shift):
                    messagebox.showerror("Error", "Shift must be in HH:MM-HH:MM format with valid times.")
                    return
                employee_id = int(employee_id)
                result = self.add_schedule(self.schedules, employee_id, date, shift)
                self.display_output(result)
                self.clear_entry_fields()
            elif self.current_action == "view_schedules_employee":
                employee_id = self.entries["employee_id"].get().strip()
                if not employee_id.isdigit():
                    messagebox.showerror("Error", "Employee ID must be a number.")
                    return
                employee_id = int(employee_id)
                result = self.view_schedules_for_employee(self.schedules, employee_id)
                self.display_output(result)
                self.clear_entry_fields()
            elif self.current_action == "view_schedules_date":
                date = self.entries["date"].get().strip()
                if not re.match(r"\d{4}-\d{2}-\d{2}", date):
                    messagebox.showerror("Error", "Date must be in YYYY-MM-DD format.")
                    return
                result = self.view_schedules_for_date(self.schedules, date)
                self.display_output(result)
                self.clear_entry_fields()
            elif self.current_action == "update_schedule":
                employee_id = self.entries["employee_id"].get().strip()
                date = self.entries["date"].get().strip()
                new_shift = self.entries["new_shift"].get().strip()
                if not employee_id.isdigit():
                    messagebox.showerror("Error", "Employee ID must be a number.")
                    return
                if not re.match(r"\d{4}-\d{2}-\d{2}", date):
                    messagebox.showerror("Error", "Date must be in YYYY-MM-DD format.")
                    return
                if not self.validate_shift(new_shift):
                    messagebox.showerror("Error", "New shift must be in HH:MM-HH:MM format with valid times.")
                    return
                employee_id = int(employee_id)
                result = self.update_schedule(self.schedules, employee_id, date, new_shift)
                self.display_output(f"Schedule updated for employee {employee_id} on {date}." if result else f"No schedule found for employee {employee_id} on {date}.")
                self.clear_entry_fields()
            elif self.current_action == "remove_schedule":
                employee_id = self.entries["employee_id"].get().strip()
                date = self.entries["date"].get().strip()
                if not employee_id.isdigit():
                    messagebox.showerror("Error", "Employee ID must be a number.")
                    return
                if not re.match(r"\d{4}-\d{2}-\d{2}", date):
                    messagebox.showerror("Error", "Date must be in YYYY-MM-DD format.")
                    return
                employee_id = int(employee_id)
                result = self.remove_schedule(self.schedules, employee_id, date)
                self.display_output(f"Schedule for employee {employee_id} on {date} removed." if result else f"No schedule found for employee {employee_id} on {date}.")
                self.clear_entry_fields()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def add_applicant(self, applicants, name, email, position_applied):
        new_id = len(applicants) + 1
        applicant = {
            "id": new_id,
            "name": name,
            "email": email,
            "position_applied": position_applied,
            "status": "Applied"
        }
        applicants.append(applicant)
        return f"Applicant {name} added with ID {new_id} and applied for {position_applied}"

    def add_employee(self, employees, name, email, position):
        new_id = len(employees) + 10
        employee = {
            "id": new_id,
            "name": name,
            "email": email,
            "position": position,
            "onboarded": False
        }
        employees.append(employee)
        return f"Employee {name} added with ID {new_id}"

    def find_applicant_by_name(self, applicants, search_name):
        results = []
        search_lower = search_name.lower()
        for applicant in applicants:
            name_lower = applicant["name"].lower()
            if search_lower in name_lower:
                results.append(applicant)
        if results:
            return "\n".join(str(applicant) for applicant in results)
        return f"No applicants found with name containing '{search_name}'."

    def find_applicant_by_id(self, applicants, applicant_id):
        for applicant in applicants:
            if applicant["id"] == applicant_id:
                return str(applicant)
        return None

    def remove_applicant(self, applicants, applicant_id):
        for i, applicant in enumerate(applicants):
            if applicant["id"] == applicant_id:
                del applicants[i]
                return True
        return False

    def mark_employee_onboarded(self, employees, employee_id):
        for employee in employees:
            if employee["id"] == employee_id:
                employee["onboarded"] = True
                return True
        return False

    def list_all_applicants(self, applicants):
        if not applicants:
            return "No applicants in the system."
        return "\n".join(str(applicant) for applicant in applicants)

    def list_all_employees(self, employees):
        if not employees:
            return "No employees in the system."
        return "\n".join(str(employee) for employee in employees)

    def hire_applicant(self, applicants, employees, applicant_id):
        for i, applicant in enumerate(applicants):
            if applicant["id"] == applicant_id:
                applicant["status"] = "Hired"
                new_employee_id = len(employees) + 101
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
                        "Certificates": False
                    }
                }
                employees.append(employee)
                del applicants[i]
                return True
        return False

    def complete_onboarding_task(self, employees, employee_id, task):
        for employee in employees:
            if employee["id"] == employee_id:
                if task in employee.get("onboarding_tasks", {}):
                    employee["onboarding_tasks"][task] = True
                    return True
                return False
        return False

    def receive_document(self, employees, employee_id, document):
        for employee in employees:
            if employee["id"] == employee_id:
                if document in employee.get("documents_received", {}):
                    employee["documents_received"][document] = True
                    return True
                return False
        return False

    def check_onboarding_status(self, employees, employee_id):
        for employee in employees:
            if employee["id"] == employee_id:
                output = f"Onboarding status for {employee['name']}:\nTasks:\n"
                for task, done in employee.get("onboarding_tasks", {}).items():
                    status = "Done" if done else "Pending"
                    output += f"  {task}: {status}\n"
                output += "Documents:\n"
                for doc, received in employee.get("documents_received", {}).items():
                    output += f"  {doc}: {'Received' if received else 'Missing'}\n"
                return output
        return f"Employee ID {employee_id} not found."

    def time_to_minutes(self, time_str, base_date):
        dt = datetime.strptime(f"{base_date} {time_str}", "%Y-%m-%d %H:%M")
        if time_str < "12:00" and time_str >= "00:00":
            dt += timedelta(days=1)  # Assume times before noon are next day for overnight shifts
        return dt.hour * 60 + dt.minute

    def shifts_overlap(self, shift1, shift2, date):
        start1, end1 = shift1.split("-")
        start2, end2 = shift2.split("-")
        start1_min = self.time_to_minutes(start1, date)
        end1_min = self.time_to_minutes(end1, date)
        start2_min = self.time_to_minutes(start2, date)
        end2_min = self.time_to_minutes(end2, date)

        # Adjust for overnight shifts
        if end1_min < start1_min:
            end1_min += 24 * 60  # Add 24 hours for overnight
        if end2_min < start2_min:
            end2_min += 24 * 60

        return not (end1_min <= start2_min or end2_min <= start1_min)

    def add_schedule(self, schedules, employee_id, date, shift):
        for schedule in schedules:
            if schedule["employee_id"] == employee_id and schedule["date"] == date:
                if self.shifts_overlap(schedule["shift"], shift, date):
                    return f"Error: Employee {employee_id} already has an overlapping shift on {date}: {schedule['shift']}"
        schedule = {
            "employee_id": employee_id,
            "date": date,
            "shift": shift
        }
        schedules.append(schedule)
        return f"Schedule added for employee {employee_id} on {date} for {shift}."

    def view_schedules_for_employee(self, schedules, employee_id):
        found = False
        output = ""
        for schedule in schedules:
            if schedule["employee_id"] == employee_id:
                output += str(schedule) + "\n"
                found = True
        if not found:
            return f"No schedules found for employee {employee_id}."
        return output

    def view_schedules_for_date(self, schedules, date):
        found = False
        output = ""
        for schedule in schedules:
            if schedule["date"] == date:
                output += str(schedule) + "\n"
                found = True
        if not found:
            return f"No schedules found for {date}."
        return output

    def update_schedule(self, schedules, employee_id, date, new_shift):
        for schedule in schedules:
            if schedule["employee_id"] == employee_id and schedule["date"] == date:
                # Check for overlaps with other schedules
                for other_schedule in schedules:
                    if (other_schedule["employee_id"] == employee_id and 
                        other_schedule["date"] == date and 
                        other_schedule != schedule):
                        if self.shifts_overlap(other_schedule["shift"], new_shift, date):
                            return False
                schedule["shift"] = new_shift
                return True
        return False

    def remove_schedule(self, schedules, employee_id, date):
        for i, schedule in enumerate(schedules):
            if schedule["employee_id"] == employee_id and schedule["date"] == date:
                del schedules[i]
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = HrAutoGui(root)
    root.mainloop()