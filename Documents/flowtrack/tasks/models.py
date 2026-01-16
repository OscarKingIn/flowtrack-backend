from django.db import models
from workflows.models import Workflow

class Task(models.Model):
    STATUS_CHOICES = (
        ("todo", "Todo"),
        ("doing", "Doing"),
        ("done", "Done"),
    )

    workflow = models.ForeignKey(
        Workflow,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
