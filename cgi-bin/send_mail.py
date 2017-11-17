#! /usr/bin/env python


from cgimply.header import headers
from cgimply.template import template
from cgimply.request import POST
from smtp_mail import send_mail


headers({
    "Content-type" : "text/html;charset=utf-8"
})


template(
    """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Document</title>
            <link href="/static/css/send_mail.css" rel="stylesheet" type="text/css">
        </head>
        <body>
            <div class="content">
                <h1>Отправка сообщения...</h1>
                <img src="/static/img/tornado.gif" alt="Загрузка" width="300" height="300">
                <h2>{result}</h2>
                <h2><a href="/cgi-bin/form_mail.py">Назад</a></h2>
            </div>
        </body>
        </html>
    """,
    {
        "result" : send_mail(POST)
    }
)
