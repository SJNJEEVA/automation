import sqlite3    
import datetime
import smtplib
from email.message import EmailMessage

# Step 1 : Create db for User requests

# Connect (or create) your SQLite database file
conn = sqlite3.connect("user_query.db")
cursor = conn.cursor()

#  Create the approval history table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    amount TEXT,
    status TEXT,          
    timestamp TEXT
)
""")

conn.commit()

# Step 2 : fill thoses table columns with user data
def link_user_data(name,email,amount):
    time = datetime.datetime.now().isoformat()

    cursor.execute(
        'INSERT INTO user_history (name,email,amount,timestamp) VALUES (?,?,?,?)',
        (name,email,amount,time)
    )
    conn.commit()
    print('User data logged in the database')

# step 3 : establish smtp connection and notify the user
def notify(to_email, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = 'vijayjeeva8@gmail.com'
    sender_password = "xkmo yzus miwd xvkv" 

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email 
    msg['To'] = to_email
    msg.set_content(body)

    # SMTP connection
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

# step 4 : check if the amount is grater than 100 for all rows in db and email the user
def approval():
    cursor.execute(
        'SELECT id,name,email,amount,status FROM user_history'
    )
    rows = cursor.fetchall()

    for row in rows:
        row_id,name,email,amount,status = row

        if int(amount) >= 100:
            status='Approved'
            #notify(to_email=email,
                   #subject='Approval',
                   #body='The amount has been approved')
            
            print('Notification sent')
            
        else:
            status='Not Approved'
            
        cursor.execute(
            'UPDATE user_history SET status=? WHERE id=?  AND (status IS NULL OR status = "")',(status,row_id)
            )
        
        
    conn.commit()
    print("Approval status updated for all records.")

link_user_data(name='Check',email='hi@gmail.com',amount=50)    
approval() 




    

    



