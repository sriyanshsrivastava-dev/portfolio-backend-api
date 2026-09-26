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