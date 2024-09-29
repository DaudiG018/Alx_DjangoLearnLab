from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        user = super().post(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user=user.user)
        return Response({'token': token.key})

