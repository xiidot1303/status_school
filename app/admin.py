from django.contrib import admin
from app.models import *

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree', 'phone')


admin.site.register(Application, ApplicationAdmin)