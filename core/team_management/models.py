from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.TextField("First name", max_length=50)
    last_name = models.TextField("Last name", max_length=50)
    email = models.EmailField("Email", max_length=100)
    phone_number = models.TextField("Phone Number", max_length=13)
    is_admin = models.BooleanField("Admin Account", default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name