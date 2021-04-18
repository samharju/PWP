from django.urls import path, include

from rest_framework import routers

from users.views import UserViewSet, ObtainAuthTokenWithControls


router = routers.DefaultRouter()
router.register('', UserViewSet, basename='user')
app_name = 'users'

urlpatterns = [
    path('token', ObtainAuthTokenWithControls.as_view(), name='token'),
    path('', include(router.urls))
]
