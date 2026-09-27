from django.contrib import admin
from project.models import Project, Technology, Skill, Media


# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'project_type')
    search_fields = ('title',)
    list_display_links = ('id','title')
    list_filter = ('created_at',)



@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id','name','type')
    search_fields = ('name',)
    list_display_links = ('id','name')
    list_filter = ('name',)



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
    list_display_links = ('id','name')
    list_filter = ('name',)



@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'url','type')
    search_fields = ('title',)
    list_display_links = ('id','title')
    list_filter = ('title','type',)