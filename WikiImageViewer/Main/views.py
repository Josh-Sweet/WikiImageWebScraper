from django.shortcuts import render
from django.forms import modelform_factory
from DataModels.models import WikiPage
from .collect import collect

# The form model for session data.
form = modelform_factory(WikiPage, exclude=[])


# Renders the session form model and manages the input
def MainPage(request):
    if request.method == "POST":
        # Should sanitized first
        URLform = form(request.POST)
        if URLform.is_valid():
            # Gets all the image URLs.
            images = collect(URLform.cleaned_data['URL'])
            # Renders the image page wih all of the images gathered on it.
            return render(request, "Main/images.html", {"images": images})
    else:
        URLform = form()
    return render(request, "Main/MainPage.html", {"form": form})
