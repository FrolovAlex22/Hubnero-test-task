from django.urls import path
from . import views


app_name = "current_usd"

urlpatterns = [
    path("get-current-usd/", views.get_current_rate, name="get_current_usd"),
]
