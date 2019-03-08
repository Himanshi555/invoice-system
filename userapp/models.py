from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Email = models.EmailField(max_length=255)

    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.Email)






@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


@property
def full_name(self):
    return "{} {}".format(self.first_name, self.last_name)

User.add_to_class('full_name', full_name)



class Employee(models.Model):
    Name = models.CharField(max_length=50,null=False,blank=False)
    Email = models.EmailField(max_length=250,blank=False)
    Address = models.TextField(max_length=265,null=False, blank=True)
    Image = models.ImageField(null=True,blank=True)
    Position = models.CharField(max_length=50,null=True,blank=True)
    salary = models.IntegerField(default=0, null=True,blank=True)
    date_added = models.DateTimeField(default=datetime.now)


    def __str__(self):
       return self.Name

class Customer(models.Model):
    Name = models.CharField(max_length=50,null=False,blank=False)
    Email = models.EmailField(max_length=265,blank=False)
    Address = models.TextField(max_length=265,null=False, blank=True)
    Wallet = models.PositiveIntegerField()



    def __str__(self):
       return '%s' % self.username
