from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UsersSerializer


class RegisterUser(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UsersSerializer

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
