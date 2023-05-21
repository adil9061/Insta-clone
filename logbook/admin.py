from django.contrib import admin
from logbook.models import Post
from logbook.models import Like
from logbook.models import Follow
from logbook.models import profile

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(profile)
