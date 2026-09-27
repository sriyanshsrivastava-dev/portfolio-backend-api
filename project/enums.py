from django.db import models


class Status(models.TextChoices):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    ARCHIVED = "ARCHIVED"
    DROPPED = "DROPPED"


class ProjectType(models.TextChoices):
    PERSONAL = "PERSONAL"
    ACADEMIC = "ACADEMIC"
    OPEN_SOURCE = "OPEN_SOURCE"
    CLIENT = "CLIENT"

class MediaType(models.TextChoices):
    VIDEO = "VIDEO"
    IMAGE = "IMAGE"
    GIF = "GIF"
    PDF = "PDF"
    OTHER = "OTHER"

class TechnologyType(models.TextChoices):
    LANGUAGE = "LANGUAGE"
    FRAMEWORK = "FRAMEWORK"
    LIBRARY = "LIBRARY"
    DATABASE = "DATABASE"
    PLATFORM = "PLATFORM"
    RUNTIME = "RUNTIME"
    OTHER = "OTHER"
    TOOLS = "TOOLS"

