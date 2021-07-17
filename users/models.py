from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, BaseUserManager
from django.contrib.auth.password_validation import *

""" class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10) """
""" 
""" 
class MyUserManager(BaseUserManager):
    def create_user(self,username,phone_number,password):
        if not username:
            raise ValueError("User must have an username")
        if not phone_number:
            raise ValueError("User must have a phone number")
        validate_password(password)
        user = self.model(username=username,phone_number=phone_number)    
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,phone_number,password):
        user = self.create_user(username=username,phone_number=phone_number,password=password)    
        user.is_admin = True
        user.is_staff = True
        usergit ini.is_superuser = True
        user.save(using=self._db)
        return user
          


class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=10,unique=True)
    username = models.CharField(max_length = 30, unique = True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length = 100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number',]

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True 


 



""" class User(models.Model):
 
    username = models.CharField( max_length = 30, blank = False,
                                 null = False)
     

 """