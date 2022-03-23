from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class Tutorial(models.Model):
    author = models.ForeignKey(User, related_name='author',on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
    
