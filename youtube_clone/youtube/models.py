from django.db import models

class Comment(models.Model): 
    comment = models.CharField(max_length=300)
    response = models.CharField(max_length=300)
