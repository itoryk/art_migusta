from django.urls import path

from application.feedback import views
from application.feedback.apps import FeedbackConfig

app_name = FeedbackConfig.label

urlpatterns = [
    path("", views.FeedbackView.as_view(), name="index")
]