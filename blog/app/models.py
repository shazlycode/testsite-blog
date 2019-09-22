from django.db import models
from django .utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_name = models.CharField(max_length=100)
    post_body = models.TextField(default="")
    email = models.EmailField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post_name
    
    class Meta:
        ordering = ('-post_date',)
