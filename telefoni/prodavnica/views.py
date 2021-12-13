import rest_framework
from django.contrib.auth.hashers import check_password
from django.http import request
from rest_framework import generics, status, authentication, exceptions, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Telefon
from prodavnica.serializers import TelefonSerializer, UserTelefonSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate, login


class AdminAuthenticationPermission(permissions.BasePermission):
    ADMIN_ONLY_AUTH_CLASSES = [rest_framework.authentication.BasicAuthentication,
                               rest_framework.authentication.SessionAuthentication]

    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated:
            return user.is_superuser or\
                   not any(isinstance(request._authenticator, x) for x in self.ADMIN_ONLY_AUTH_CLASSES)
        return False


class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": RegisterSerializer(user, context=self.get_serializer_context()).data
        })


class Login(APIView):
    def post(self, request):
        user = User.objects.filter(username=request.data['username']).first()

        if not check_password(request.data['password'], user.password):
            return Response({"message": "Invalid password.", "status": status.HTTP_400_BAD_REQUEST})
        else:
            return Response({"message": "Success.", "status": status.HTTP_200_OK})


class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, AdminAuthenticationPermission,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, AdminAuthenticationPermission,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = 'username'

    def myview(self, request):
        username = [obj.usr for obj in User.objects.all()]
        return request, {'username': username}


class UserTelefonList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserTelefonSerializer


class UserTelefonDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserTelefonSerializer


class TelefonList(generics.ListCreateAPIView):
    queryset = Telefon.objects.all()
    serializer_class = TelefonSerializer


class TelefonDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, AdminAuthenticationPermission,)
    queryset = Telefon.objects.all()
    serializer_class = TelefonSerializer


class TelefonBy(generics.ListAPIView):
    serializer_class = TelefonSerializer

    def get_queryset(self):
        queryset = Telefon.objects.filter(naziv=self.kwargs.get('naziv'))
        return queryset
