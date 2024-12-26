import streamlit as st
import pandas as pd
from email_sender import send_personalized_emails
from database import update_database, get_recruiters, create_tables, clear_all_recruiters
from scheduler import start_email_scheduler, update_schedule_time, read_schedule_time
from log import get_email_logs, create_log_table, clear_all_logs

def main():
    st.title("Email Sender Application")

    menu = ["Home", "Database Viewer", "Email Logs", "Scheduler Settings"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

        # Upload CSV file
        csv_file = st.file_uploader("Upload CSV file", type=["csv"])
        
        if csv_file is not None:
            df = pd.read_csv(csv_file)
            required_columns = {"Name", "Email", "Company", "IsCMR"}
            if not required_columns.issubset(df.columns):
                st.error(f"CSV file must contain the following columns: {', '.join(required_columns)}")
            else:
                st.write("Data Preview:")
                st.dataframe(df)

                # Update database with CSV data
                if st.button("Update Database"):
                    try:
                        update_database(df)
                        st.success("Database updated successfully!")
                    except Exception as e:
                        st.error(f"Failed to update database: {e}")

        # Send personalized emails
        if st.button("Send Emails"):
            recruiters = get_recruiters()
            if recruiters:
                try:
                    send_personalized_emails("eligetivignesh@gmail.com", "ahjz yiex munj vdjl", "D:/Mine/Vignesh Eligeti Resume.pdf")
                    st.success("Emails sent successfully!")
                except Exception as e:
                    st.error(f"Failed to send emails: {e}")
            else:
                st.error("No recruiters found in the database.")

    elif choice == "Database Viewer":
        st.subheader("Database Viewer")
        recruiters = get_recruiters()
        if recruiters:
            df = pd.DataFrame(recruiters, columns=["ID", "Name", "Email", "Company", "isCMR"])
            st.dataframe(df)
        else:
            st.error("No recruiters found in the database.")

        # Clear all recruiters
        if st.button("Clear All Recruiters"):
            try:
                clear_all_recruiters()
                st.success("All recruiters have been removed from the database.")
            except Exception as e:
                st.error(f"Failed to clear recruiters: {e}")

    elif choice == "Email Logs":
        st.subheader("Email Logs")
        logs = get_email_logs()
        if logs:
            df = pd.DataFrame(logs, columns=["ID", "Recipient", "Email", "Time"])
            st.dataframe(df)
        else:
            st.error("No email logs found.")

        # Clear all logs
        if st.button("Clear All Logs"):
            try:
                clear_all_logs()
                st.success("All email logs have been removed from the database.")
            except Exception as e:
                st.error(f"Failed to clear logs: {e}")

    elif choice == "Scheduler Settings":
        st.subheader("Scheduler Settings")
        current_time = read_schedule_time()
        st.write(f"Current Schedule Time: {current_time}")

        new_time = st.text_input("New Schedule Time (HH:MM)", current_time)
        if st.button("Update Schedule Time"):
            try:
                update_schedule_time(new_time)
                st.success(f"Schedule time updated to {new_time}")
            except Exception as e:
                st.error(f"Failed to update schedule time: {e}")

if __name__ == "__main__":
    create_tables()  # Ensure recruiters table exists
    create_log_table()  # Ensure email_logs table exists
    start_email_scheduler()  # Start the email scheduler when the program starts
    main()