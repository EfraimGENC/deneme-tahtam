from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    birthday = models.DateField('Birthday', null=True, blank=True)

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return "{} {}".format(self.first_name, self.last_name)
        else:
            return self.username

    @full_name.setter # Full name in boşluktan sonraki son kelimesini last_name, önsesini first_name e kadeder.
    def full_name(self, value):
        names = value.split(' ')
        self.first_name = " ".join(names[:-1])
        self.last_name = "".join(names[-1])

    def save(self, *args, **kwargs): 
        self.username = self.email # Username'i email olarak kaydediyor. Email zaten uniqe.
        super(User, self).save(*args, **kwargs) 