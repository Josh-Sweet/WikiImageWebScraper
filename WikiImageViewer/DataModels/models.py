from django.db import models


# WikiPage class. Just contains the name of the page.
class WikiPage(models.Model):
    URL = models.CharField(max_length=2058)

    def __str__(self):
        return f"{self.URL}"
