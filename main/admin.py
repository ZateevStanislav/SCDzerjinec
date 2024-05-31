from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('time_create', 'is_published')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'phone_number')

admin.site.register(News, NewsAdmin)
admin.site.register(Student, StudentAdmin)

