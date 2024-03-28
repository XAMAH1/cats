from random import randint
from threading import Thread

from send_mail.send.send import send, send_message
from send_mail.config import *


class send_mail:
    def send_code_register(self, send_adress):
        code = randint(100000, 999999)
        message = f"Добро пожаловать в программу CatsShop! Мы рады видеть, что вы присоединяетесь к нашему сообществу. Для того чтобы завершить процесс регистрации и пользоваться всеми привилегиями нашей программы, просим вас ввести уникальный код, который мы предоставили вам ниже. Необходимость ввода кода гарантирует нашу индивидуальную идентификацию каждого участника и обеспечивает безопасность наших данных."
        subject = "Код подтверждения регистрации"
        Thread(target=send, args=(send_adress, code, smtp_password, from_email, smtp_server, smtp_port, message, subject, )).start()
        return code


    def send_code(self, send_adress, operation=None):
        code = randint(100000, 999999)
        message = f"Вы начали {operation} в программе CatsShop. Введите код."
        subject = "Код подтверждения операции"
        Thread(target=send, args=(send_adress, code, smtp_password, from_email, smtp_server, smtp_port, message, subject, )).start()
        return code

    def send_message(self, send_adress, message, subject):
        Thread(target=send_message,
               args=(send_adress, smtp_password, from_email, smtp_server, smtp_port, message, subject,)).start()