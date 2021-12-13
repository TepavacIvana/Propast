from django.contrib.auth import authenticate
from rest_framework import serializers
from prodavnica.models import User, Telefon
from django.contrib.auth.hashers import make_password


class UserTelefonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefon
        fields = ('naziv',)


class RegisterSerializer(serializers.ModelSerializer):
    telefon = UserTelefonSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'telefon')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(RegisterSerializer, self).create(validated_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data


class TelefonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class TelefonSerializer(serializers.ModelSerializer):
    owner = TelefonUserSerializer(read_only=True)

    class Meta:
        model = Telefon
        fields = ('owner', 'naziv', 'model', 'boja', 'cena', 'radnja')

