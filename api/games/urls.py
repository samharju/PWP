from django.urls import include, path
from rest_framework.routers import DefaultRouter

from games.views import GameViewSet


router = DefaultRouter()
router.register('', GameViewSet, basename='game')
app_name = 'games'

urlpatterns = [
    path('', include(router.urls))
]
