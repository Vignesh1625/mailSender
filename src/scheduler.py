import schedule
import time
import threading
from email_sender import send_personalized_emails

def job():
    # Replace with your email and password
    sender_email = "eligetivignesh@gmail.com"
    sender_password = "ahjz yiex munj vdjl"
    attachment_path = "D:/Mine/Vignesh Eligeti Resume.pdf"
    send_personalized_emails(sender_email, sender_password,attachment_path)

def read_schedule_time():
    try:
        with open("schedule_time.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        # Set default time to 09:00 if file does not exist
        with open("schedule_time.txt", "w") as file:
            file.write("09:00")
        return "09:00"

def start_email_scheduler():
    schedule_time = read_schedule_time()
    schedule.every().day.at(schedule_time).do(job)

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

def update_schedule_time(new_time):
    with open("schedule_time.txt", "w") as file:
        file.write(new_time)
    schedule.clear()
    schedule.every().day.at(new_time).do(job)