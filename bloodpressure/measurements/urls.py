from django.urls import path
from . import views

app_name = "measurements"

urlpatterns = [
    path("", views.list, name="list"),
    path("<int:id>/", views.measurements_details, name="details")
]