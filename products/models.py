from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title