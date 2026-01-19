from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Workflow
from .serializers import WorkflowSerializer

class WorkflowViewSet(ModelViewSet):
    serializer_class = WorkflowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Workflow.objects.filter(
            project__owner=self.request.user
        )
