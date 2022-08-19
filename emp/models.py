from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmpDetails(models.Model):
    user_id = models.AutoField(primary_key=True, default=None)
    user_key = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, default=None, null=True, blank=True)
    user_email = models.EmailField(unique=True, blank=True, null=True)
    user_password = models.CharField(max_length=100, default=None, blank=True)
    user_image = models.ImageField(upload_to ='uploads/', height_field=None, width_field=None, max_length=100)
    user_phone = models.CharField(max_length=15, unique=True, default=None, null=True, blank=True)
    user_address = models.CharField(max_length=255, default=None)

    def __str__(self):
        return str(self.user_name)
