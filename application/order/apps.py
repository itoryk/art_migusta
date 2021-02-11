from django.apps import AppConfig


class OrderConfig(AppConfig):
    label = "order"
    name = f'application.{label}'


