from django.urls import path

from demo.views import HelloView

urlpatterns = [
    path("", HelloView.as_view()),
]
