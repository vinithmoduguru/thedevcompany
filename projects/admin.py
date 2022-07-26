from django.contrib import admin

# Register your models here.
from .models import Project, Reviews, Tag

admin.site.register(Project)
admin.site.register(Reviews)
admin.site.register(Tag)
