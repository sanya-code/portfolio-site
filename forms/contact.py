import streamlit as st
import smtplib
import re
from email.message import EmailMessage

# Store these in .streamlit/secrets.toml
EMAIL_ADDRESS = st.secrets["EMAIL_USER"]
EMAIL_PASSWORD = st.secrets["EMAIL_PASS"]
RECEIVER_EMAIL = st.secrets["RECEIVER_EMAIL"]

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not name or not email or not message:
            st.error("All fields are required.")
            return

        if not is_valid_email(email):
            st.error("Invalid email address.")
            return

        try:
            # Compose the email
            msg = EmailMessage()
            msg["Subject"] = f"New Message from {name}"
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = RECEIVER_EMAIL
            msg.set_content(
                f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            )

            # Send email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            st.success("Your message has been sent successfully! 📬")

        except Exception as e:
            st.error(f"Failed to send message. Error: {str(e)}")
