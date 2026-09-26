from django.db import models
from .enums import *

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    short_description = models.TextField()
    description = models.TextField()
    problem_statement = models.TextField()
    solution = models.TextField()
    status = models.CharField(choices=Status, default=Status.ACTIVE, max_length=15)
    project_type = models.CharField(choices=ProjectType, default=ProjectType.PERSONAL, max_length=15)
    start_date = models.DateField()
    end_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    display_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
