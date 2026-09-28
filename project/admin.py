from django.contrib import admin
from infrastructure.media_tools.filename import HexFileNameGenerator
from infrastructure.media_tools.processor import ImageProcessor
from infrastructure.media_tools.uploader import LocalFileUploader
from project.forms import MediaAdminForm
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
    form = MediaAdminForm
    exclude = ["url"]

    def save_model(self, request, obj, form, change):
        uploaded_file = form.cleaned_data.get('upload')

        if uploaded_file:
            file_name = HexFileNameGenerator.generate(extension="webp")
            processed_image = ImageProcessor.resize(uploaded_file,(1920,1080))
            file_to_upload = processed_image or uploaded_file
            obj.url = LocalFileUploader.upload(
                file=file_to_upload,
                file_name=file_name
            )

        super().save_model(request, obj, form, change)


