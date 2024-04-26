from django.db import models


# Create your models here.
class savingaccount(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    mobile_number = models.IntegerField()
    addhar_number = models.IntegerField()
    password = models.CharField(max_length=24)
    Account_type = models.CharField(max_length=20)
    ocupation = models.CharField(max_length=20)
    a_number = models.IntegerField(null=True)
    salary = models.FloatField(null=True)
    loan = models.FloatField(null=True)
    image = models.ImageField(null=True, upload_to="uimg/")
