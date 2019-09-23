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
        
        
class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم')
    comment_body = models.TextField(verbose_name='نص التعليق')
    email = models.EmailField(verbose_name='البريد الالكتروني')
    comment_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comment')
    
    def __str__(self):
        return 'علق {} على {}'.format(self.name, self.post)
    
    class Meta:
        ordering = ('-comment_date',)
    
    
