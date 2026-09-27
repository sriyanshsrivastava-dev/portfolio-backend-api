from django.contrib import admin
from project.models import Project, Technology, Skill, Media


# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','tagline','start_date','end_date', 'project_type','created_at')
    search_fields = ('title',)
    list_display_links = ('id','title')
    list_filter = ('created_at','project_type','status','is_published','featured')
    exclude = ['slug','created_at','modified_at']



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