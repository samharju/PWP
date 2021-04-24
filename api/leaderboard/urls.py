from django.urls import path, include
from rest_framework import routers

from leaderboard.views import LeaderViewSet

router = routers.DefaultRouter()
router.register('', LeaderViewSet, basename='user')
app_name = 'leaderboard'

urlpatterns = [
    path('', include(router.urls))
]
