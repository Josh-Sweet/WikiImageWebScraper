from django.urls import path
from Main.views import MainPage

# Contains the pattern to the main page.
urlpatterns = [
    path('', MainPage, name="MainPage"),
]
