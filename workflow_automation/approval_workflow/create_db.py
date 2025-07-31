import sqlite3

# Connect (or create) your SQLite database file
conn = sqlite3.connect("approvals.db")
cursor = conn.cursor()

# Create the approval history table if it doesn't exist
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
