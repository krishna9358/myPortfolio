from django.contrib import admin
from .models import Post



class MemberAdmin(admin.ModelAdmin):
    list_display = ("title", "author")

# Register your models here.
admin.site.register(Post, MemberAdmin)