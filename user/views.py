from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer, UserRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(serializer.data['email'], serializer.data['password'], False, False)
            user.username = serializer.data['username']
            user.save()

            return Response(UserSerializer(user).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
