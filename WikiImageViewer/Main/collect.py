import requests
from bs4 import BeautifulSoup as bs


# Collects images from the wikipedia page given.
def collect(URL):
    # Gets the main URL from the gathered entry
    mainURL = "https://en.wikipedia.org/wiki/" + URL

    URLcontents = requests.get(mainURL)

    # Gets a soup object from the contents gathered from the URL
    soup = bs(URLcontents.text, features="html.parser")

    # Gets each image URL
    urls = []
    for img in soup.find_all("img"):
        imageURL = img.attrs.get("src")

        urls.append(imageURL)

    # Filters what might be bad URLs
    urls = [x for x in urls if "/static/"not in x]
    urls = [x for x in urls if ":" not in x]
    urls = [x for x in urls if "?" not in x]

    return urls
