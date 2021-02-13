from django.urls import path

from application.illustration import views
from application.illustration.apps import IllustrationConfig

app_name = IllustrationConfig.label

urlpatterns = [
    path("", views.IllustrationView.as_view(), name="index"),
    path("one/", views.IllustrationOne.as_view()),
    path("para/", views.IllustrationPara.as_view()),
    path("custom/", views.IllustrationCustom.as_view())
]