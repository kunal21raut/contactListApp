from django.db import models

class Contact(models.Model):

    full_name = models.CharField(max_length=400)
    relationship = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
