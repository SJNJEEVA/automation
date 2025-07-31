import sqlite3
import logging
import smtplib
from email.message import EmailMessage
import pandas as pd

# Setup logging (same as before)
logging.basicConfig(
    filename='automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_notification_email(to_email, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "vijayjeeva8@gmail.com"         # <-- CHANGE THIS
    sender_password = "xkmo yzus miwd xvkv"       # <-- CHANGE THIS

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

def process_row(amount):
    try:
        if amount > 0:
            return 'Valid'
        else:
            return 'Invalid'
    except Exception as e:
        logging.error(f"Error processing amount {amount}: {e}")
        return 'Error'

def main():
    try:
        logging.info("Starting automated data entry process with SQLite.")

        # Connect to database
        conn = sqlite3.connect('automation.db')
        cursor = conn.cursor()                        # activate cursor

        # Ensure Status column exists
        cursor.execute("PRAGMA table_info(requests)")
        columns = [info[1] for info in cursor.fetchall()]               # cursor.fetchall() method returns all rows from the most recent executed query as a list of tuples. you must call fetchall() only after a SELECT or any query that returns rows.
        if 'Status' not in columns:
            cursor.execute("ALTER TABLE requests ADD COLUMN Status TEXT")

        # Get all pending or NULL status rows
        cursor.execute("SELECT id, Name, Email, Amount FROM requests")  # we used SELECT to return row with only those selected columns, so we can fetch all rows from that selected row.
        rows = cursor.fetchall()
        logging.info(f"Fetched {len(rows)} rows from database.")

        # Process rows and update status
        for row in rows:                                # rows is a tuple that contains multiple values from one row of the database table.
            row_id, name, email, amount = row           # <--- unpacks the tuple into variables with meaningful names:
            status = process_row(amount)

            # Update Status
            cursor.execute("UPDATE requests SET Status = ? WHERE id = ?", (status, row_id))   # WHERE clause is a filter condition that specifies which rows should be updated.

        conn.commit()
        cursor.close()
        conn.close()

        logging.info("Database updated with status.")

        # Send notification email
        send_notification_email(
            to_email="jeevanandanselvaraj@gmail.com",   # Change to your recipient
            subject="Automated Data Entry Complete",
            body="The automated data entry task has finished updating the database."
        )

        logging.info("Notification email sent successfully.")
        print("Automated data entry complete. Check automation.log for details.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An unexpected error occurred: {e}. See automation.log.")

if __name__ == "__main__":
    main()




##########################################################################################

# in real-world, we use db files not like csv file, thus we connect to that file via sqlite3.connect() and do the changes in the file. 
    # therefore the file gets tweaked in itself and i dont need to output to another file like csv.

# PRAGMA table_info(table_name) is a SQLite-specific command (not standard SQL) that returns metadata about the columns of the specified table.
    # when you run cursor.execute("PRAGMA table_info(requests)"), 
        # it asks SQLite: Tell me the details of each column (name, type, etc.) in the table named requests.
            # The query returns a list of rows where each row describes one column in the requests table, usually including:
                # Column ID (an integer index)
                # Column name (string)
                # Data type (string)
                # Whether it can be NULL or not (boolean)
                # Default value (if any)
                # If it's a primary key (boolean)

    # This is useful to check if a certain column already exists in the table (like we did for the Status column).


