from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 250)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    publlished_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
