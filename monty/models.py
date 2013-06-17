from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Round(models.Model):

    player = models.CharField(max_length=50)
    prize_loc = models.IntegerField()
    first_guess = models.IntegerField()
    second_guess = models.IntegerField(null=True, blank=True)


class PrizeImages(models.Model):

    image_type = models.CharField(max_length=10,
                                    choices=[('door', 'door'),
                                                ('win', 'win'),
                                                ('lose', 'lose')])
    img = models.ImageField(upload_to='images/')
