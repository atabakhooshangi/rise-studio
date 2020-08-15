from django.contrib import admin
from django.urls import path
from .views import MembersView, VideosView, PhotosView

urlpatterns = [
    path('members', MembersView.as_view(), name='members'),
    path('photos', PhotosView.as_view(), name='photos'),
    path('videos', VideosView.as_view(), name='videos')

]
