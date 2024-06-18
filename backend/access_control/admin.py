from django.contrib import admin
from .models import Restriction, PhorgeMember, Card, CardSwipeLog


# Register your models here.
admin.site.register(Restriction)
admin.site.register(PhorgeMember)
admin.site.register(Card)
admin.site.register(CardSwipeLog)
