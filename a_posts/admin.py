from django.contrib import admin
from .models import (
    Post,
    Tag,
    Comment,
    Reply
)

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)