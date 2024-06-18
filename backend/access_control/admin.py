from django.contrib import admin
from .models import Restriction, PhorgeMember, Card, CardSwipeLog


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["last_swiped", "enabled", "uid"]


@admin.register(CardSwipeLog)
class CardSwipeLogAdmin(admin.ModelAdmin):
    list_display = ["card", "swiped_on"]


@admin.register(PhorgeMember)
class PhorgeMemberAdmin(admin.ModelAdmin):
    list_display = ["full_name", "member_until", "member_since", "last_access"]

    exclude = ["birth_date"]


# Register your models here.
admin.site.register(Restriction)
