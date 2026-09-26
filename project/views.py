from rest_framework.views import Response, APIView
from project.serializers import ProjectSerializer
from project.services import get_all_projects

# Create your views here.

class ProjectCollection(APIView):
    def get(self, request):
        projects = get_all_projects()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
