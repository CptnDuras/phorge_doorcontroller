from rest_framework import serializers
from .models import Restriction, PhorgeMember, Card, CardSwipeLog


class RestrictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restriction
        fields = "__all__"


class PhorgeMemberSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    is_current_member = serializers.ReadOnlyField()

    class Meta:
        model = PhorgeMember
        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "over_18",
            "member_until",
            "member_since",
            "last_access",
            "full_name",
            "is_current_member",
        ]


class CardSerializer(serializers.ModelSerializer):
    pretty_uid = serializers.ReadOnlyField()

    class Meta:
        model = Card
        fields = ["id", "uid", "last_swiped", "enabled", "member", "pretty_uid"]


class CardSwipeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardSwipeLog
        fields = "__all__"
