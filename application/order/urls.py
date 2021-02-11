from django.urls import path

from application.order import views
from application.order.apps import OrderConfig

app_name = OrderConfig.label

urlpatterns = [
    path("", views.OrderView.as_view(), name="index")
]