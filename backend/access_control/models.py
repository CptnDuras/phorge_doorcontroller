import uuid6
from django.db import models
from django.utils import timezone


# Create your models here.


class Restriction(models.Model):
    time_from = models.DateField()
    time_to = models.DateField()


class PhorgeMember(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    over_18 = models.BooleanField()
    member_until = models.DateField()
    member_since = models.DateField()
    last_access = models.DateTimeField(null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_current_member(self):
        if timezone.today() <= self.member_until:
            return True
        return False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid6.uuid7, editable=False)
    uid = models.BinaryField(max_length=6)
    last_swiped = models.DateTimeField(null=True, blank=True)
    enabled = models.BooleanField(default=False)

    member = models.ForeignKey(
        PhorgeMember, on_delete=models.PROTECT, null=True, blank=True
    )

    def can_access(self):
        # Eventually make this more complex - i.e. make sure anyone under 18 can access only during daylight hours
        return self.enabled

    @property
    def pretty_uid(self):
        return ":".join(format(byte, "02x") for byte in bytes(self.uid))

    def __str__(self):
        if self.member is not None:
            return f"{self.member.full_name}({self.pretty_uid}), last swiped: {self.last_swiped}"
        return f"({self.pretty_uid}), last swiped: {self.last_swiped}"


class CardSwipeLog(models.Model):
    card = models.ForeignKey(Card, on_delete=models.PROTECT)
    swiped_on = models.DateTimeField(default=timezone.now())
    unlock = models.BooleanField()
