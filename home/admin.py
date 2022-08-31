import imp
from django.contrib import admin
from home.models import Contact
from .models import video, video_10, video_11ip, video_11cs,video_12ip,video_12cs
from embed_video.admin import AdminVideoMixin

class AdminVideo(AdminVideoMixin,admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Contact)
admin.site.register(video,AdminVideo)
admin.site.register(video_10,AdminVideo)
admin.site.register(video_11ip,AdminVideo)
admin.site.register(video_11cs,AdminVideo)
admin.site.register(video_12ip,AdminVideo)
admin.site.register(video_12cs,AdminVideo)