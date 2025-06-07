# 📨 Python Auto Email Scheduler

This is an automated email scheduler built using Python. It sends styled HTML emails (with optional attachments) to multiple recipients at a specific time daily.

## ✅ Features:
- Sends emails via Gmail using App Password
- HTML formatting and emojis in body
- Optional file attachment
- Auto-scheduling using `schedule` module
- Creates desktop confirmation file
- Logging included
- Runs automatically on system startup

## 📂 Files:
- `auto_emailer.py`: Main script
- `email_log.txt`: Sample log output
- `startup_check.txt`: Confirms the script started

## 🚀 Tools Used:
- Python 3
- schedule
- smtplib
- email.mime
- logging
- ctypes (for message box)

## ⚙️ How It Works:
1. Set your Gmail and App Password
2. Add recipient emails
3. Schedule time using `schedule.every().day.at("HH:MM")`
4. Run the script or add it to system startup

---

