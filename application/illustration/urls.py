from django.urls import path

from application.illustration import views
from application.illustration.apps import IllustrationConfig

app_name = IllustrationConfig.label

urlpatterns = [
    path("", views.IllustrationView.as_view(), name="index")
]