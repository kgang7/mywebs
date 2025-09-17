from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return " {} - {}".format(self.title,self.id)
    
    