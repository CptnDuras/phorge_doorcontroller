from datetime import datetime

import uuid6
from django.db import models

# Create your models here.


class Restriction(models.Model):
    time_from = models.DateField()
    time_to = models.DateField()


class PhorgeMember(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    over_18 = models.BooleanField()
    member_until = models.DateField()
    member_since = models.DateField()
    last_access = models.DateTimeField()

    @property
    def is_current_member(self):
        if datetime.now() <= self.member_until:
            return True
        return False


class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid6.uuid7(), editable=False)
    uid = models.BinaryField(max_length=6)
    last_swiped = models.DateTimeField()
    enabled = models.BooleanField(default=False)

    member = models.ForeignKey(PhorgeMember, on_delete=models.PROTECT, null=True, blank=True)

    def can_access(self):
        # Eventually make this more complex - i.e. make sure anyone under 18 can access only during daylight hours
        return self.enabled


class CardSwipeLog(models.Model):
    card = models.ForeignKey(Card, on_delete=models.PROTECT)
    swiped_on = models.DateTimeField(default=datetime.now())
    unlock = models.BooleanField()



