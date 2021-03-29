from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, blank=True)
    text = models.TextField(verbose_name='Write your review')
    rating = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)
