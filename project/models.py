from django.db import models
from .enums import Status,ProjectType, MediaType, TechnologyType

# Create your models here.
class Project(models.Model):
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,db_index=True, unique=True)
    tagline = models.CharField(max_length=200, null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    problem_statement = models.TextField(null=True,blank=True)
    motivation = models.TextField(null=True,blank=True)
    solution_summary = models.TextField(null=True,blank=True)
    key_features = models.TextField(null=True,blank=True)
    status = models.CharField(choices=Status, default=Status.ACTIVE, max_length=15)
    project_type = models.CharField(choices=ProjectType, default=ProjectType.PERSONAL, max_length=15)
    repository_url = models.CharField(max_length=300,null=True,blank=True)
    live_url = models.CharField(max_length=300,null=True,blank=True)
    featured = models.BooleanField(default=False,db_index=True)
    is_published = models.BooleanField(default=False,db_index=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    media = models.ManyToManyField("Media", related_name="projects",blank=True)
    technologies = models.ManyToManyField("Technology", related_name="projects",blank=True)
    skills = models.ManyToManyField("Skill", related_name="projects",blank=True)


class Media(models.Model):
    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=300)
    type = models.CharField(choices=MediaType, default=MediaType.IMAGE, max_length=15)
    alt_text = models.CharField(max_length=300,null=True,blank=True)
    caption = models.TextField(null=True,blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    description = models.TextField(null=True,blank=True)


class Technology(models.Model):
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
    name = models.CharField(max_length=200, db_index=True, unique=True)
    type = models.CharField(choices=TechnologyType, max_length=50)

    def __str__(self):
        return self.name

