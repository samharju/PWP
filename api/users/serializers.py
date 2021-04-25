from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

from core.serializers import MasonItemSerializer


user_schema = {
    "type": "object",
    "properties": {
        "password": {
            "type": "string"
        }
    },
    "required": ["password"]
}


class UserItemSerializer(MasonItemSerializer):
    """Serializer for the users object"""

    def create_controls(self, instance, request):
        self_href = reverse('users:user-detail', request=request, args=(instance.pk,))
        author_query = f'?author={instance.pk}'
        controls = {
            'self': {
                'description': "Main menu",
                'href': self_href
            },
            'collection': {
                'description': "List of Users",
                'href': reverse('users:user-list', request=request)
            },
            'history': {
                'description': "User's history",
                'href': 'todo'
            },
            'rules-created': {
                'description': "List of Rules",
                'href': reverse('rules:rule-list', request=request) + author_query,
            }
        }
        if instance == request.user:
            controls.update(
                **{
                    'edit': {
                        'description': "Modify User",
                        'href': self_href,
                        'method': 'PUT',
                        'schema': user_schema
                    },
                    'delete': {
                        'description': "Remove User",
                        'href': self_href,
                        'method': 'DELETE'
                    }
                }
            )
        return controls

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'win_percentage', 'wins', 'losses')
        read_only_fields = ('win_percentage', 'wins', 'losses')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, encrypt password if updated"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class UserUpdateSerializer(UserItemSerializer):

    class Meta:
        model = get_user_model()
        fields = ('password',)


class UserCollectionSerializer(UserItemSerializer):

    def create_controls(self, instance, request):
        self_href = reverse('users:user-detail', request=request, args=(instance.pk,))
        return {
            'self': {
                'description': "Current User",
                'href': self_href
            }
        }
