import sqlite3
import datetime

# Connect to the SQLite database (can be moved outside the class for efficiency)
conn = sqlite3.connect("approvals.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS approval_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workflow_id INTEGER,
    step_index INTEGER,
    role TEXT,
    approver TEXT,
    status TEXT,
    timestamp TEXT
)
""")
conn.commit()

class ApprovalWorkflow:
    def __init__(self, workflow_id,steps):
        # steps is a list of tuples (role, name) representing the approval steps in order
        self.workflow_id = workflow_id  
        self.steps = steps
        self.current_step = 0
        self.approvals = [False] * len(steps)

    def log_status_to_db(self, step_index, role, approver, status):
        timestamp = datetime.datetime.now().isoformat()
        cursor.execute(
            "INSERT INTO approval_history (workflow_id, step_index, role, approver, status, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
            (self.workflow_id, step_index, role, approver, status, timestamp)
        )
        conn.commit()

    def approve(self, approver_name):
        # Approve the current step if the approver matches
        if self.current_step >= len(self.steps):
            return "Workflow already complete."
        
        role, name = self.steps[self.current_step]
        
        if name == approver_name:
            self.approvals[self.current_step] = True
            self.log_status_to_db(self.current_step, role, name, "Approved")  # Log approval
            self.current_step += 1
            
            if self.current_step == len(self.steps):
                return "All approvals complete. Workflow approved."
            else:
                next_role, next_name = self.steps[self.current_step]
                return f"Step approved by {approver_name}. Next approval required from {next_role} ({next_name})."
        
        else:
            return f"Approval denied. Current approval step requires {role} ({name}), not {approver_name}."

    def status(self):
        status_list = []
        
        for i, (role, name) in enumerate(self.steps):
            status_str = f"{role} ({name}): " + ("Approved" if self.approvals[i] else "Pending")
            
            if i == self.current_step and not self.approvals[i]:
                status_str += " <- Current Step"
            
            status_list.append(status_str)
        return "\n".join(status_list)
    
def get_workflow_history(workflow_id):
    
    cursor.execute(
        "SELECT step_index, role, approver, status, timestamp FROM approval_history WHERE workflow_id=? ORDER BY step_index, timestamp",
        (workflow_id,)
    )
    
    records = cursor.fetchall()
    
    for record in records:
        step_index, role, approver, status, timestamp = record
        print(f"Step {step_index}: {role} ({approver}) - {status} at {timestamp}")

# Define the approval steps and approvers (you can customize as needed)
steps = [
    ("Manager", "Alice"),
    ("Finance", "Bob"),
    ("Director", "Charlie")
]
workflow_id =1

# Initialize the workflow
workflow = ApprovalWorkflow(workflow_id,steps)

# Sample usage and demonstration:
print(workflow.status())            # Initial status
print(workflow.approve("Alice"))   # Manager Alice approves
print(workflow.status())            # Status after Alice approves
print(workflow.approve("Eve"))     # Wrong approver tries to approve
print(workflow.approve("Bob"))     # Finance Bob approves
print(workflow.status())            # Status after Bob approves
print(workflow.approve("Charlie")) # Director Charlie approves
print(workflow.status())            # Final status

get_workflow_history(workflow_id)
