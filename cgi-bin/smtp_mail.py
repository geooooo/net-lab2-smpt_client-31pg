"""
    Модуль работы с почтой по протоколу SMTP
"""


from socket import socket
from base64 import b64encode


def send_mail(data):
    """
        Отправка сообщения на почту
    """

    # Хост и порт SMTP-сервера
    HOST = "mail.edm-core.ru"
    PORT = 587
    TIMEOUT = 5
    MSG_LEN = 1024
    LOGIN = "test@edm-core.ru"
    MAIL = "test@edm-core.ru"
    PWD = "123qwerty123"

    # Обработка данных формы
    to = data["to"].strip()
    theme = data["theme"].strip()
    message = data["message"].strip()

    # Создание сокета
    client_socket = socket()
    client_socket.settimeout(TIMEOUT)
    client_socket.connect((HOST, PORT))

    # Подключение к почтовому серверу
    code_server_name, *other = client_socket.recv(MSG_LEN).decode("utf-8").split(" ")
    code, *server_name = code_server_name.split("-")
    server_name = "-".join(server_name)
    if code != "220":
        client_socket.close()
        return "Ошибка при подключении к почтовому серверу !"

    client_socket.send(("EHLO " + server_name + "\n").encode("utf-8"))
    code, *other = client_socket.recv(MSG_LEN).decode("utf-8").split("-")
    if code != "250":
        client_socket.close()
        return "Ошибка при идентификации клиента !"

    # Авторизация клиента
    client_socket.send(("AUTH LOGIN\n").encode("utf-8"))
    code, *other = client_socket.recv(MSG_LEN).decode("utf-8").split()
    if code != "334":
        client_socket.close()
        return "Не удалось авторизоваться на сервере !"
    client_socket.send(b64encode(LOGIN.encode("utf-8")) + b"\n")
    code, *other = client_socket.recv(MSG_LEN).decode("utf-8").split()
    if code != "334":
        client_socket.close()
        return "Не удалось авторизоваться на сервере !"
    client_socket.send(b64encode(PWD.encode("utf-8")) + b"\n")
    code, *other = client_socket.recv(MSG_LEN).decode("utf-8").split()
    if code != "235":
        client_socket.close()
        return "Не удалось авторизоваться на сервере !"

    # Отправка почты
    client_socket.send(("MAIL FROM:" + MAIL + "\n").encode("utf-8"))
    code, *other = client_socket.recv(MSG_LEN).decode("utf-8").split()
    if code != "250":
        client_socket.close()
        return "Не удалось отправить сообщение !"
    client_socket.send(("RCPT TO:" + to + "\n").encode("utf-8"))
    code, *other = client_socket.recv(MSG_LEN).decode("utf-8").split()
    if code != "250":
        client_socket.close()
        return "Не удалось отправить сообщение !"
    client_socket.send((b"DATA\n"))
    code, *other = client_socket.recv(MSG_LEN).decode("utf-8").split()
    if code != "354":
        client_socket.close()
        return "Не удалось отправить сообщение !"
    client_socket.send(
        "From:{0}\nTo:{1}\nSubject:{2}\n\n{3}\n.\n".format(MAIL, to, theme, message).encode("utf-8")
    )
    code, *other = client_socket.recv(MSG_LEN).decode("utf-8").split()
    if code != "250":
        client_socket.close()
        return "Не удалось отправить сообщение !"

    # Завершение отправки почты
    client_socket.send(b"QUIT")
    return "Сообщение отправлено !"
