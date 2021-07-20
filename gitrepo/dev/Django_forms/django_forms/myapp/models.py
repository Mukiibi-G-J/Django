from django.db import models


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    boby = models.TextField()
    
    
    def __str__(self): 
        return self.name
