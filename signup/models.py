from django.db import models

# Create your models here.

#prebuilt id/pk autoconfigurator
class Company(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=32)
    logo = models.CharField(max_length=512)


#Jobs that are taken by the company
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE())
    type = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    num_of_workers = models.IntegerField(default=1)