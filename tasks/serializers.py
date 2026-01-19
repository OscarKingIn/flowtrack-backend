from rest_framework import serializers
from .models import Task
from workflows.serializers import WorkflowSerializer

class TaskSerializer(serializers.ModelSerializer):
    workflow = WorkflowSerializer(read_only=True)
    workflow_id = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.model.workflow.field.related_model.objects.all(),
        source='workflow', write_only=True
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'workflow', 'workflow_id', 'created_at']