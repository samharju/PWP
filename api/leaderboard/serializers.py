from django.contrib.auth import get_user_model

from rest_framework import serializers


class LeaderSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'win_percentage', 'wins', 'losses')
        read_only_fields = ('username', 'win_percentage', 'wins', 'losses')
 
