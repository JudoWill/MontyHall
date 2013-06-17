from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Round(models.Model):

    user = models.ForeignKey(User)
    prize_loc = models.IntegerField()
    first_guess = models.IntegerField()
    second_guess = models.IntegerField(null=True, blank=True)


class PrizeImages(models.Model):

    winning_prize = models.BooleanField(default=False)
    img = models.ImageField(upload_to='images/')
