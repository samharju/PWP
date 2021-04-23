from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class EntryPoint(APIView):

    permission_classes = []

    def get(self, request, format=None):
        response = {
            "@controls": {
                "create-user": {
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
                        "href": "todo"
                    },
                    "games": {
                        "href": reverse('games:game-list', request=request),
                    },
                    "rules": {
                        "href": reverse('rules:rule-list', request=request),
                    }
                }
            }
        return Response(response)
