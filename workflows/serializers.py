from rest_framework import serializers
from .models import Workflow
from projects.serializers import ProjectSerializer

class WorkflowSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Workflow.objects.model.project.field.related_model.objects.all(),
        source='project', write_only=True
    )

    class Meta:
        model = Workflow
        fields = ['id', 'name', 'project', 'project_id']