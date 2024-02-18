from django.db import models

class svk(models.Model):
    icon=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TimeField()
    
    

# Create your models her