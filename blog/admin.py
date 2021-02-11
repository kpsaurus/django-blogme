from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

# Register your models here.

from .models import (Post, Tag, Category)


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Post, SomeModelAdmin)
admin.site.register([Tag, Category])
admin.site.site_header = "BlogMe! Admin"
admin.site.site_title = "BlogMe!"
admin.site.index_title = "Welcome to BlogMe!"
