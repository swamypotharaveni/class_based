from django.db import models
from django.urls import reverse
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    uplode_images=models.ImageField(upload_to = 'pic_folder/',null=True,blank=True)



