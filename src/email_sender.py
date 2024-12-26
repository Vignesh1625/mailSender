import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from database import get_recruiters
from log import log_email
from datetime import datetime
import sqlite3

def send_personalized_emails(sender_email, sender_password, attachment_path):
    """
    Sends personalized emails to recruiters from the SQLite database.

    Args:
        sender_email (str): Your email address.
        sender_password (str): Your email password (or app-specific password if using Gmail).
        attachment_path (str): Path to the file you want to attach.
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email, company, is_cmr FROM recruiters')
    rows = cursor.fetchall()

    for row in rows:
        id, name, email, company, is_cmr = row  # Unpack the values
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = "Application for Internship Opportunity – Vignesh Eligeti"

        body = f"""Dear {name},

My name is Vignesh Eligeti, and I am currently in my fourth year pursuing a B-Tech degree from CMR College of Engineering and Technology. Over the past few years, I have worked as a freelance developer and completed several notable projects. Additionally, I served as a board member of the Entrepreneur Club at my college, which has further enhanced my skills and experience.

Some of my key projects include:

    Medical Hunt : A medical college search engine developed in collaboration with Crew Labs. Link: https://medicalhunt.in/
    SAMAM : A project focused on medical health assessment tools.
    Dynamic Length : A length predictor for e-commerce platforms like Amazon and Flipkart.

I am proficient in languages such as Java, Python, and SQL, and I have experience with various frameworks like Flask, Django, Spring Boot. My expertise lies in backend development and deep learning analysis. I believe I am well-suited for internships because of my strong technical foundation and proven ability to execute real-world projects. My experience working on diverse projects demonstrates my ability to adapt to new challenges and deliver results effectively. As a quick learner with a collaborative mindset, I am confident that I can contribute positively to your team and gain valuable experience while fulfilling the responsibilities of the role.

I am attaching my resume for your review. Thank you for considering my application.

Sincerely,

Vignesh Eligeti
"""
        msg.attach(MIMEText(body, 'plain'))

        # Attach the file
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={attachment_path.split('/')[-1]}",
        )
        msg.attach(part)

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, email, text)
            server.quit()
            print(f"Email sent to {name} at {email}")
            log_email(name, email, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        except Exception as e:
            print(f"Failed to send email to {name} at {email}: {e}")

    conn.close()