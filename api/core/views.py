import json
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class EntryPoint(APIView):

    permission_classes = []

    def get(self, request, format=None):
        response = {
            "@controls": {
                "create-user": {
                    'description': "Create new user",
                    "href": reverse('users:user-list', request=request),
                    "method": "POST",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "username": {
                                "type": "string"
                            },
                            "password": {
                                "type": "string"
                            }
                        }
                    }
                },
                "auth-token": {
                    'description': "Get token for user",
                    "href":  reverse('users:token', request=request),
                    "method": "POST",
                    "schema": {
                        "username": {
                            "type": "string"
                        },
                        "password": {
                            "type": "string"
                        }
                    }
                }
            }
        }
        if request.user and request.user.is_authenticated:
            response = {
                "@controls": {
                    "leaderboard": {
                        'description': "Leaderboard",
                        "href": reverse('leaderboard:user-list', request=request),
                    },
                    "games": {
                        'description': "Games",
                        "href": reverse('games:game-list', request=request),
                    },
                    "rules": {
                        'description': "Rules",
                        "href": reverse('rules:rule-list', request=request),
                    },
                    "users": {
                        'description': "Users",
                        "href": reverse('users:user-list', request=request),
                    }
                }
            }
        return Response(response)


with open("openapi.json") as f:
    data = json.load(f)


class Schema(APIView):
    permission_classes = []

    def get(self, request):
        return Response(data=data)
