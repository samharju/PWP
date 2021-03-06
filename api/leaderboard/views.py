from rest_framework.reverse import reverse
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from leaderboard.serializers import LeaderSerializer

from core.models import User


class LeaderViewSet(GenericViewSet):
    """Get list of users sorted by win percentage."""
    queryset = User.objects.all().order_by("-win_percentage")
    serializer_class = LeaderSerializer

    permission_classes = []

    def list(self, request, *args, **kwargs):
        """Serve only get requests"""
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response = {
            'items': serializer.data,
            '@controls': {
                'up': {
                    'href': reverse('entrypoint', request=request),
                    'description': "Main menu",
                },
                'users': {
                    'href': reverse('users:user-list', request=request),
                    'description': "List of users",
                }
            }
        }
        return Response(response)
