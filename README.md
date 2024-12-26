# emailSender/emailSender/README.md

# Email Sender Application

This project is a Streamlit application designed to facilitate the sending of personalized emails to recruiters. It allows users to upload a CSV file containing recruiter information, update an SQLite database, send emails, and schedule daily email tasks.

## Features

- Upload a CSV file containing recruiter names and email addresses.
- Update an SQLite database with the information from the uploaded CSV file.
- Send personalized emails to each recruiter.
- Schedule daily email tasks for sending emails automatically.

## Project Structure

```
emailSender
├── src
│   ├── app.py               # Main entry point for the Streamlit application
│   ├── email_sender.py      # Logic for sending personalized emails
│   ├── database.py          # SQLite database management
│   ├── scheduler.py         # Scheduling of email tasks
│   └── utils
│       └── __init__.py      # Utility functions
├── requirements.txt         # Required Python libraries
├── README.md                # Project documentation
└── .streamlit
    └── config.toml         # Streamlit configuration settings
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd emailSender
   ```

2. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

2. Follow the on-screen instructions to upload your CSV file, send emails, and schedule tasks.

## Requirements

- Python 3.x
- Streamlit
- Pandas
- SQLite3
- Schedule
- SMTPLIB

## License

This project is licensed under the MIT License.