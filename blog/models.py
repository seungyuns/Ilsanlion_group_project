# from django.conf import settings
from django.db import models

# Create your models here.
class Blog(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:20]    

    
            
    
    
