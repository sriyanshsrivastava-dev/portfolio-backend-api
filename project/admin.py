from django.contrib import admin
from project.models import Project

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'project_type')
    search_fields = ('title',)
    list_display_links = ('id','title')
    list_filter = ('created_at',)