from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class AlcoholType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Alcohol(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    volt = models.IntegerField()
    votes = models.IntegerField()
    type = models.ForeignKey(AlcoholType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_alcohol = models.ManyToManyField(Alcohol)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Komentarz użytkownika {self.user.username} o {self.alc.name}"


class Wine(models.Model):
    alcohol = models.OneToOneField(Alcohol, on_delete=models.CASCADE)

    dryness = models.CharField(max_length=24)
    color = models.CharField(max_length=24)


