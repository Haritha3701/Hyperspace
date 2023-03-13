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

class comments(models.Model):
    pro=models.ForeignKey(plans,related_name="cmt",on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    msg=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    