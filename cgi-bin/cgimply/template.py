"""
    Предоставление функционала шаблонизации
"""


def template(text, kwargs={}):
    """
        Заполнение шаблона данными
    """
    print(text.format(**kwargs))
