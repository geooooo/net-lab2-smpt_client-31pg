"""
    Модуль отправки заголовков ответа
"""


def header(name, value):
    """
        Отправка заголовка
    """
    print("{0}:{1}".format(name, value))


def headers(kwargs):
    """
        Отправка нескольких заголовков
    """
    print(kwargs)
    for name in kwargs:
        header(name, kwargs[name])
    print()
