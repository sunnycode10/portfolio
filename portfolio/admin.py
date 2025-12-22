from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'live_link')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('order',)
