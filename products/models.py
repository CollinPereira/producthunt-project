from django.db import models

# Create your models here.

class product(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    votes_total=models.IntegerField()
    image=models.ImageField(upload_to='images/')

