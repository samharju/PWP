from django.db.models import ProtectedError
from rest_framework import mixins, permissions, status
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import GenericViewSet

from api.error_handlers import mason_error
from core.models import Rule
from rules.serializers import RuleDetailSerializer, RuleListSerializer


class OwnerEditOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.author


create_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'description': 'rule name',
            'type': 'string'
        },
        'rows': {
            'description': 'number of rows',
            'type': 'integer',
            'minimum': 3,
            'maximum': 10
        },
        'columns': {
            'description': 'number of columns',
            'type': 'integer',
            'minimum': 3,
            'maximum': 10
        },
        'winning_tick_count': {
            'description': 'number of ticks to get in line to win',
            'type': 'integer',
            'minimum': 3,
            'maximum': 10
        },
    }
}


class RuleViewSet(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin):

    queryset = Rule.objects.all()
    permission_classes = [IsAuthenticated, OwnerEditOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        if (username := self.request.query_params.get('author')) is not None:
            return queryset.filter(author__username=username)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return RuleListSerializer
        return RuleDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_success_headers(self, data):
        return {'Location': data['@controls']['self']['href']}

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = None
        return response

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
        except ProtectedError:
            return mason_error("Can't remove rule that has been used in a game")
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_success_headers(self, data):
        return {'Location': data['@controls']['self']['href']}

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
                    'description': "Create rule",
                    'href': reverse('rules:rule-list', request=request),
                    'method': 'POST',
                    'schema': create_schema
                }
            }
        }
        return Response(response)
