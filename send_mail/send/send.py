import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from send_mail.send import send_html, send_message_html


def send(send_adress, code, smtp_password, from_email, smtp_server, smtp_port, message, subject):  # Код подтверждения
    to_email = send_adress
    msg = MIMEMultipart()
    msg["From"] = f"CatsShop <{from_email}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    html_body = send_html.get_code(message, code)
    msg.attach(MIMEText(html_body, "html"))
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        try:
            server.login(from_email, smtp_password)
            server.send_message(msg)
        except Exception as e:
            pass
    return


def send_message(send_adress, smtp_password, from_email, smtp_server, smtp_port, message, subject):  # Обычное сообщение
    to_email = send_adress
    msg = MIMEMultipart()
    msg["From"] = f"CatsShop <{from_email}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    html_body = send_message_html.get_code(message)
    msg.attach(MIMEText(html_body, "html"))
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        try:
            server.login(from_email, smtp_password)
            server.send_message(msg)
        except Exception as e:
            pass
    return
