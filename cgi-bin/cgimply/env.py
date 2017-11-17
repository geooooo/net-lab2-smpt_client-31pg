"""
    Модуль упрощённого доступа к переменным окружения
"""


import os


# Формирование словаря с переменными окружения
ENV = {var.upper():os.environ[var] for var in os.environ}
