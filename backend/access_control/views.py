from rest_framework import viewsets
from .models import Restriction, PhorgeMember, Card, CardSwipeLog
from .serializers import (
    RestrictionSerializer,
    PhorgeMemberSerializer,
    CardSerializer,
    CardSwipeLogSerializer,
)


class RestrictionViewSet(viewsets.ModelViewSet):
    queryset = Restriction.objects.all()
    serializer_class = RestrictionSerializer


class PhorgeMemberViewSet(viewsets.ModelViewSet):
    queryset = PhorgeMember.objects.all()
    serializer_class = PhorgeMemberSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardSwipeLogViewSet(viewsets.ModelViewSet):
    queryset = CardSwipeLog.objects.all()
    serializer_class = CardSwipeLogSerializer
