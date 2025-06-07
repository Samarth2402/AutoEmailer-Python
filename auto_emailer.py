import schedule
import time
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import ctypes

# ✅ Show a pop-up to confirm script has started
ctypes.windll.user32.MessageBoxW(0, "📨 Auto Emailer started successfully!", "Python AutoMailer", 1)

# ✅ Create a file on Desktop to confirm it ran
with open("C:/Users/ADMIN/Desktop/startup_check.txt", "w") as f:
    f.write("Script started successfully at login.\n")

# ✅ Setup logging
logging.basicConfig(filename='email_log.txt',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("🚀 Script started on login.")

sender_email = "ss9879086402@gmail.com"
app_password = "funmwcbgkdlxcmcc"

# ✅ List of recipients
receiver_emails = [
    "samartha240057@gmail.com",
    "mcab240009@gmail.com"
]

subject = "Scheduled Email with Attachment and HTML"

html_body = """
<html>
  <body>
    <h2 style="color:blue;">Hello,</h2>
    <p>This is an <b>automated email</b> sent by Python script.</p>
    <p>Hope you have a great day! 😊</p>
  </body>
</html>
"""

# ✅ Set attachment path or keep empty
attachment_path = ""  # Example: "C:/path/to/file.pdf"

def send_email():
    try:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ", ".join(receiver_emails)
        message["Subject"] = subject

        # Attach HTML body
        message.attach(MIMEText(html_body, "html"))

        # Add attachment if available
        if attachment_path and os.path.isfile(attachment_path):
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}")
            message.attach(part)

        # Send email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_emails, message.as_string())
        server.quit()

        logging.info(f"✅ Email sent successfully to {receiver_emails}")
        print(f"✅ Email sent successfully to {receiver_emails}")

    except Exception as e:
        logging.error(f"❌ Failed to send email: {e}")
        print(f"❌ Failed to send email: {e}")

# ✅ Schedule the email (testing at 13:00 / 1 PM)
schedule.every().day.at("13:20").do(send_email)

print("⏳ Scheduler started. Waiting to send emails...")

while True:
    schedule.run_pending()
    time.sleep(1)
