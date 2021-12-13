from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=30, unique=True, blank=False)
    username = models.CharField(max_length=30, unique=True, blank=False)
    password = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return str(self.username)


class Telefon(models.Model):
    naziv = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    boja = models.CharField(max_length=30)
    cena = models.IntegerField()
    radnja = models.CharField(max_length=50)
    owner = models.ForeignKey(User, related_name='telefon', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Telefon, self).save(*args, **kwargs)                              #proveri jel ovo treba

    def __str__(self):
        return str(self.naziv)



