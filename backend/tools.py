import smtplib
import requests

def send_email(to, subject, message):
    return f"Email would be sent to {to} with subject '{subject}'."

def send_sms(number, text):
    return f"SMS would be sent to {number}. Content: {text}"

def web_search(query):
    return f"Simulated search results for: {query}"

