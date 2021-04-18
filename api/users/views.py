from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import BasePermission
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer

from core.models import User


class AnonCreateAndUpdateOwnerOnly(BasePermission):
    """
    Inspired from:
    https://github.com/encode/django-rest-framework/issues/1067

    Custom permission:
        - allow anonymous POST
        - allow authenticated PUT, DELETE on *own* record
    """

    def has_permission(self, request, view):
        return view.action == 'create' or request.user and \
               request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['destroy', 'update', 'partial_update']:
            return obj == request.user
        return True


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AnonCreateAndUpdateOwnerOnly]


class ObtainAuthTokenWithControls(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data.update(
            **{
                '@controls': {
                    'up': {
                        'href': reverse('entrypoint', request=request)
                    }
                }
            }
        )
        return response
