import streamlit as st
import os
import smtplib
import ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'rommeldm87@gmail.com'
    password = os.getenv('PASSWORD')
    receiver = 'rommeldm87@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


print(os.getcwd())

st.header('Contact Me')


with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message here")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
