from django.urls import path, include

from rest_framework import routers

#from leaderboard.views import LeaderViewSet,ObtainAuthTokenWithControls
from leaderboard.views import LeaderViewSet

router = routers.DefaultRouter()
router.register('', LeaderViewSet, basename='user')
app_name = 'leaderboard'

urlpatterns = [
    #path('token', ObtainAuthTokenWithControls.as_view(), name='token'),
    path('', include(router.urls))
]
