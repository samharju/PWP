from rest_framework import permissions, mixins
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import GenericViewSet

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
        queryset = self.queryset
        username = self.request.query_params.get('author')
        if username is not None:
            queryset = queryset.filter(author__username=username)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return RuleListSerializer
        return RuleDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

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
