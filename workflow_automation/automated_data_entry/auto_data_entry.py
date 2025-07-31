import pandas as pd
import re

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


################# check the valid email ################

def is_valid_email(email):
    pattern = r"^[^@]+@[^@]+\.[^@]+$"
    return re.match(pattern, email) is not None

# For demonstration: let's validate 'Amount' > 0, and add a 'Status' column
def process_row(row):
    try:
       # Check required fields
        if not row['Name'] or not row['Email']:
            return 'Missing Required Field or extra char'
        
          # Validate email format
        if not is_valid_email(row['Email']):
            print(f"Invalid email: {row['Email']}")
            return 'Invalid Email'

       # Validate amount
        amount = float(row['Amount'])
        if amount > 10000:
            return 'Flag for Review'
        elif amount > 0:
            return 'Valid'
        else:
            return 'Invalid'

    except (ValueError, KeyError) as e:
        logging.error(f"Error processing row {row}: {e}")
        return 'Error'
    

########### lets add email notification ##############

import smtplib                                       # SMTP stands for Simple Mail Transfer Protocol and it is the standard protocol used for sending emails across the Internet.
from email.message import EmailMessage               # The email module is a built-in Python module to help compose, parse, and handle email messages easily and EmailMessage is a class inside email.message that simplifies creating an email message including headers and body. 

def send_notification_email(to_email, subject, body):
    # Configure your email credentials/settings here
    smtp_server = "smtp.gmail.com"                   # smtp_server is a string that specifies the address of the SMTP server you want to use to send emails.
    smtp_port = 587                                  # smtp_port is the port number on which the SMTP server listens for connections.For Gmail's SMTP with TLS, the port is usually 587.
    sender_email = "vijayjeeva8@gmail.com"          
    sender_password = "xkmo yzus miwd xvkv"          # your application password

    msg = EmailMessage()                             # EmailMessage() creates a new email message object that you can set headers (From, To, Subject) and the message content (body).
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email
    msg.set_content(body)                            # set_content() is a method of the EmailMessage object and It sets the main body text of the email message.For example, msg.set_content("Hello!") sets the email body to "Hello!".

    # Establish a secure session with the server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:    # Using with automatically opens the connection and ensures it is properly closed when done (even if errors occur).
        server.starttls()                                   # Stands for "Start Transport Layer Security". It upgrades the connection with the SMTP server to be encrypted (secure). This is important because emails and credentials should be sent over an encrypted connection.
        server.login(sender_email, sender_password)         # Authenticates you to the SMTP server, You provide your email address and password (or app password) to prove you are allowed to send emails using that account.
        server.send_message(msg)                            # Sends the EmailMessage object you created (msg) through the SMTP server to the recipient(s). This actually transmits the email out.
    print("Notification email sent!")

# smtplib.SMTP() creates an SMTP client session object connected to the SMTP server.
    # Arguments:
        # smtp_server (string): The domain name or IP of the SMTP server (e.g., "smtp.gmail.com").
        # smtp_port (int): The port number on which to connect (e.g., 587).

    # This SMTP client session object allows your script to communicate with the email server to send messages.

############### lets add logging #######################

import logging                                               # logging is a built-in Python module for recording messages that describe program execution. It helps track events, errors, warnings, and info messages during runtime.

# Setup logging
logging.basicConfig(
    filename='automation.log',                               # specifies log output file.
    level=logging.INFO,                                      # level=logging.INFO: means log only messages with level INFO or higher (INFO, WARNING, ERROR, CRITICAL). DEBUG messages will be ignored.
    format='%(asctime)s - %(levelname)s - %(message)s'       # formatting string defining how each log line looks.
)

# logging.basicConfig() configures the logging system. It sets:
    # Arguments:
        # Where to store logs (file, console, etc.)
        # What minimum level of messages to log (e.g. DEBUG, INFO, WARNING, ERROR, CRITICAL)
        # How the logged messages look (format)
            # %(asctime)s: timestamp of the log message
            # %(levelname)s: severity level (INFO, ERROR, etc.)
            # %(message)s: the actual log message
                # The %() placeholders are format specifiers that get replaced with actual data when the log is written.


#################### LOGIC #####################

def main():
    try:
        logging.info("Starting automated data entry process.")       # logging.info() is a function that writes a log message with the level INFO.

        # Read the input CSV
        input_data = pd.read_csv('input.csv')
        logging.info(f"Read {len(input_data)} rows from input.csv")

        # Process and validate data
        input_data['Status'] = input_data.apply(process_row, axis=1) # axis=1 tells pandas to apply the function process_row to each row of the DataFrame, Each row is passed as an argument to process_row(row) along with its coulmn names as a key

        # Write the results to output.csv
        input_data.to_csv('output.csv', index=False)
        logging.info(f"Output saved to output.csv")

        # Send notification email
        send_notification_email(
            to_email="jeevanandanselvaraj@gmail.com",   # Who should be notified?
            subject="Automated Data Entry Complete",
            body="The automated data entry task has finished and output.csv is ready."
        )

        logging.info("Notification email sent successfully.")
        print("Automated data entry complete. Check automation.log for details.")

    except FileNotFoundError:
        logging.error("input.csv file not found! Process aborted.")
        print("Error: input.csv file not found. Check automation.log for details.")
    except pd.errors.EmptyDataError:
        logging.error("input.csv is empty or malformed.")
        print("Error: input.csv is empty or malformed. Check automation.log.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An unexpected error occurred: {e}. See automation.log.")

if __name__ == "__main__":     # This checks whether the Python file is being run directly (not imported as a module).
    main()                     # If the script is run directly, it calls the main() function to start the process. If the file is imported from another script, the code inside this block does not run automatically.
                               # This is a common Python idiom for scripts that can be both executed standalone or imported for reuse.

################################################################################################

# .apply() method in pandas is used to apply a function along either axis (rows or columns) of a DataFrame.
    # .apply() needs your function to return a value for each row.
    # Syntax:
        # DataFrame.apply(function, axis=0 or 1)
            # axis=0 means apply to each column.
            # axis=1 means apply to each row.

