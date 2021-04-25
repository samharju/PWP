from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserCollectionSerializer, UserItemSerializer, user_schema

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
        if view.action in ['destroy', 'update']:
            return obj == request.user
        return True


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AnonCreateAndUpdateOwnerOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return UserCollectionSerializer
        return UserItemSerializer

    def get_success_headers(self, data):
        return {'Location': data['@controls']['self']['href']}

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = None
        return response

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response = {
            'items': serializer.data,
            '@controls': {
                'up': {
                    'description': "Main menu",
                    'href': reverse('entrypoint', request=request),
                },
                'create': {
                    'description': "Create new user",
                    'href': reverse('users:user-list', request=request),
                    "method": "POST",
                    "schema": user_schema,
                }
            }
        }
        return Response(response)


class ObtainAuthTokenWithControls(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data.update(
            **{
                '@controls': {
                    'up': {
                        'description': "Main menu",
                        'href': reverse('entrypoint', request=request)
                    }
                }
            }
        )
        return response
