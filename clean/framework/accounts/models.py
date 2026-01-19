from django.db import models

class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'customer'