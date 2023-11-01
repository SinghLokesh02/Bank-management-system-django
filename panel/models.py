from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_length=50)
    contact = models.TextField(max_length=50)
    account_no = models.TextField()
    balance = models.IntegerField()
    account_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name