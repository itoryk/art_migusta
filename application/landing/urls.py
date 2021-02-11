from django.urls import path

from application.landing import views
from application.landing.apps import LandingConfig

app_name = LandingConfig.label

urlpatterns = [
    path("", views.IndexView.as_view(), name="index")
]

