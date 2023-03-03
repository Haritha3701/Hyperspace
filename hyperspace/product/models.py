from django.db import models

# Create your models here.
class plans(models.Model):
    amount=models.CharField(max_length=200)
    duration=models.IntegerField()
    img=models.ImageField(upload_to="pic")
    speed=models.FloatField()
    data=models.CharField(max_length=200)
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)