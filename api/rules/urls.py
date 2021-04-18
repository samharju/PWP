from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rules.views import RuleViewSet


router = DefaultRouter()
router.register('', RuleViewSet, basename='rule')
app_name = 'rules'

urlpatterns = [
    path('', include(router.urls))
]
