from django.db import models

# Create your models here.
class complainRequest(models.Model):
    id = models.AutoField(primary_key=True)
    victim = models.CharField(max_length=100)
    discrption = models.TextField()
    address = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100)
    name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    files=models.FileField(upload_to='files/',null=True,blank=True)