from django.contrib import admin

# Register your models here.
from .models import Uploader, File

admin.site.register(Uploader)
admin.site.register(File)