from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # 🔐 ownership enforcement
    def get_queryset(self):
        return Task.objects.filter(
            workflow__project__owner=self.request.user
        )


    # ✅ filtering, search, ordering
    from django_filters.rest_framework import DjangoFilterBackend
    from rest_framework import filters
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "status"]
    ordering = ["-created_at"]
