from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    summary = models.TextField(default='Summary')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_details', args=[str(self.id)])
