from django.urls import path
from Main.views import main_page

# Contains the pattern to the main page.
urlpatterns = [
    path('', main_page, name="MainPage"),
]
