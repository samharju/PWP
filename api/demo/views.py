from rest_framework.views import APIView
from rest_framework.response import Response


class HelloView(APIView):
    def get(self, request, format=None):
        return Response("Hello!")

    def post(self, request, format=None):
        return Response(data=request.data)
