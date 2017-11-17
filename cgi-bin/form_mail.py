#! /usr/bin/env python


from cgimply.header import headers
from cgimply.template import template


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
            <link href="/static/css/form_mail.css" rel="stylesheet" type="text/css">
        </head>
        <body>
            <div class="content">
                <h1>Отправка сообщения по SMTP</h1>
                <form class="table-form" action="{action}" method="post">
                    <div class="table-form-row">
                        <label class="table-form-cell" for="text">Получатель:</label>
                        <div class="table-form-cell">
                            <input type="text" name="to">
                        </div>
                    </div>
                    <div class="table-form-row">
                        <label class="table-form-cell" for="text">Тема:</label>
                        <div class="table-form-cell">
                            <input type="text" name="theme">
                        </div>
                    </div>
                    <div class="table-form-row">
                        <label class="table-form-cell" for="text">Сообщение:</label>
                        <div class="table-form-cell">
                            <textarea name="message"></textarea>
                        </div>
                    </div>
                    <div class="table-form-row">
                        <div class="table-form-cell"></div>
                        <div class="table-form-cell">
                            <input type="submit" value="Отправить">
                        </div>
                    </div>
                </form>
            </div>
        </body>
        </html>
    """,
    {
        "action" : "/cgi-bin/send_mail.py"
    }
)
