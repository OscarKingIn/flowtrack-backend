from django.db import models
from projects.models import Project

class Workflow(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="workflows"
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
