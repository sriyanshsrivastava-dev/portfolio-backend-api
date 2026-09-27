from rest_framework import serializers
from project.models import Project, Technology, Skill, Media


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True,read_only=True)
    skills = SkillSerializer(many=True,read_only=True)
    media = MediaSerializer(many=True,read_only=True)
    class Meta:
        model = Project
        fields = "__all__"