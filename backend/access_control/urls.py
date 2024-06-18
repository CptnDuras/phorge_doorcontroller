from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RestrictionViewSet,
    PhorgeMemberViewSet,
    CardViewSet,
    CardSwipeLogViewSet,
)

router = DefaultRouter()
router.register(r"restrictions", RestrictionViewSet)
router.register(r"phorge-members", PhorgeMemberViewSet)
router.register(r"cards", CardViewSet)
router.register(r"card-swipe-logs", CardSwipeLogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
