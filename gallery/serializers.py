from rest_framework import serializers
from .models import Members, Videos, Photos


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('id', 'full_name', 'instagram', 'phone_number', 'description')


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('id', 'title', 'category', 'video')


class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ('id', 'title', 'category', 'image')
