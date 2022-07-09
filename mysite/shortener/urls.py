from django.urls import path

# Import views
from . import views

appname = "shortener"

urlpatterns = [
    # Index view
    path("", views.index, name="index"),
    path("<str:shortened_part>", views.redirect, name="redirect"),
]