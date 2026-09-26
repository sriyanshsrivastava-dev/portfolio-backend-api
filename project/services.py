from project.models import Project


def get_all_projects():
    projects = Project.objects.all()
    return projects
