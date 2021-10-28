import datetime

from django.db import models
from django.utils import timezone

class formation(models.Model):
    T20 = 'T20'
    ODAY = 'ODAY'
    TEST = 'TEST'

    type_of_matches_choices = [
        (T20,'T20'),
        (ODAY,'ODAY'),
        (TEST,'TEST'),
    ]

    pub_date = models.DateTimeField('date published',auto_now_add=True)

    type_of_match = models.CharField(max_length=10, choices=type_of_matches_choices,default=T20)
    
    no_of_batsmen = models.PositiveSmallIntegerField()

    right_batsmen = models.SmallIntegerField(default=0)
    left_batsmen = models.SmallIntegerField(default=0)

    no_of_Pacer = models.PositiveSmallIntegerField()

    pacer_right = models.PositiveSmallIntegerField(default=0)
    pacer_left = models.PositiveSmallIntegerField(default=0)

    no_of_spinner = models.PositiveSmallIntegerField(default=0)

    spinner_right = models.PositiveSmallIntegerField(default=0)
    spinner_left = models.PositiveSmallIntegerField(default=0)

    no_of_wicketkeeper = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.type_of_match

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Player_formation(models.Model):
    T20 = 'T20'
    ODAY = 'ODAY'
    TEST = 'TEST'

    type_of_matches_choices = [
        (T20,'T20'),
        (ODAY,'ODAY'),
        (TEST,'TEST'),
    ]

    pub_date = models.DateTimeField('date published',auto_now_add=True)

    type_of_match = models.CharField(max_length=10, choices=type_of_matches_choices,default=T20)
    
    no_of_batsmen = models.PositiveSmallIntegerField()

    right_batsmen = models.SmallIntegerField(default=0)
    left_batsmen = models.SmallIntegerField(default=0)

    no_of_pacer = models.PositiveSmallIntegerField()

    pacer_right = models.PositiveSmallIntegerField(default=0)
    pacer_left = models.PositiveSmallIntegerField(default=0)

    no_of_spinner = models.PositiveSmallIntegerField(default=0)

    spinner_right = models.PositiveSmallIntegerField(default=0)
    spinner_left = models.PositiveSmallIntegerField(default=0)

    no_of_wicketkeeper = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.type_of_match

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


    