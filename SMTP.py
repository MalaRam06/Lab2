import smtplib
from email.mime.text import MIMEText

def main():
    sender = ""        # replace with your Gmail
    recipient = ""     # replace with a friend's email
    app_password = ""  # generate from Google account

    msg = MIMEText("Hello! This is a test email from Mala (SMTP Lab).")
    msg["Subject"] = "SMTP Lab Test"
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            print("Connecting to SMTP server...")
            server.login(sender, app_password)
            print("Logged in, sending email...")
            server.sendmail(sender, [recipient], msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print("SMTP Error:", e)

if __name__== "__main__":
    main()