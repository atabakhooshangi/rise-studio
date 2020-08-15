from django.contrib import admin
from .models import Members, Videos, Photos
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect


class MembersAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'instagram',
    ]



class PhotosAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
    ]
    search_fields = [
        'category'
    ]
    def adding_limitation(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 100:
            return False
        else:
            return True


class VideosAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
    ]
    search_fields = [
        'category'
    ]
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 3:
            return False
        else:
            return True


admin.site.register(Members, MembersAdmin)
admin.site.register(Photos, PhotosAdmin)
admin.site.register(Videos, VideosAdmin)
