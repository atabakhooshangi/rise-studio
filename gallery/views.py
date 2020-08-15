from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.status import *
from .models import Members, Videos, Photos
from .serializers import MembersSerializer, PhotosSerializer, VideosSerializer
from rest_framework.permissions import AllowAny


class MembersView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MembersSerializer
    queryset = Members.objects.all()


class PhotosView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PhotosSerializer
    queryset = Photos.objects.all()


class VideosView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = VideosSerializer
    queryset = Videos.objects.all()
