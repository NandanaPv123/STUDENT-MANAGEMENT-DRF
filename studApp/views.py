from django.shortcuts import render
from studApp.serializers import UserSerializer
from studApp.models import StudModel
from rest_framework.response import Response
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
# Create your views here.

class UserCreateView(CreateAPIView):
   serializer_class=UserSerializer
   def perform_create(self,serializer):
        return User.objects.create_user(**serializer.validated_data)


class StudentCreateListView(CreateAPIView,ListAPIView):
    serializer_class=UserSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()


class StudentRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    lookup_url_kwarg="id"

