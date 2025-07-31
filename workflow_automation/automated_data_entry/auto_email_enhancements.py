import smtplib
from email.message import EmailMessage
import os                                   # This is a built-in Python module that provides a way to interact with the operating system.

def send_notification_email(to_emails, subject, body, attachment_path=r'C:\Users\user\Desktop\VS python\go_auto\workflow_automation\automated_data_entry\automation.log'):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "vijayjeeva8@gmail.com"        # <-- CHANGE THIS
    sender_password = "xkmo yzus miwd xvkv"        # <-- CHANGE THIS

    # Create the email message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email

    # Support multiple recipients by joining emails with commas if a list is provided
    if isinstance(to_emails, list):
        msg["To"] = ", ".join(to_emails)
    else:
        msg["To"] = to_emails

    msg.set_content(body)

    # Attach file if specified and exists                       # os.path This is a submodule inside os that provides utilities to work specifically with file system paths.
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:                  # "rb" means read the file in binary mode (important for non-text files or any file you want to read as raw bytes, such as attachments).
            file_data = f.read()
            file_name = os.path.basename(attachment_path)       # This function takes a full file path (like "/home/user/docs/file.txt" or "C:\\Users\\User\\file.txt") and returns only the file name part at the end ("file.txt").
        # Add attachment with MIME type application/octet-stream (generic for any file)
        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)   

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("Notification email sent!")

send_notification_email(
        to_emails=["jeevanandanselvaraj@gmail.com",'jeeva149@outlook.com'],   # Who should be notified?
        subject="Automated Data Entry Complete",
        body="The automated data entry task has finished and output.csv is ready."
        )



#############################################################################################

# What is MIME?
    # It is a standard that defines the types of content that can be sent over email or the internet in general, like text, images, audio, video, and other files.
        # When sending emails with attachments, you need to tell the email client what type of file you’re sending (its MIME type), so it can handle it properly.
            # For example:
                # text/plain → plain text emai
                # image/jpeg → JPEG image file
                # application/pdf → PDF file
                # application/octet-stream → generic binary file (used as a fallback for unknown file types)

# add_attachment() is a method of the Python EmailMessage object from the email module. It’s used to add a file as an attachment to your email message.
    # Arguments:
        # file_data: The file content in bytes (read in binary mode).
        # maintype: The main MIME type of the file (e.g., "application" or "image").
        # subtype: The subtype under the main type (e.g., "octet-stream" for generic binary files).
        # filename: The name of the file as it will appear in the email attachment.

