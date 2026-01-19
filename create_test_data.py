#!/usr/bin/env python
"""Create test data for pagination"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowtrack.settings')
django.setup()

from projects.models import Project
from workflows.models import Workflow
from tasks.models import Task
from django.contrib.auth.models import User

# Get admin user
admin = User.objects.get(username='admin')

# Create a project for admin
project, _ = Project.objects.get_or_create(name='Admin Project', defaults={'description': 'Admin test project', 'owner': admin})
print(f'Project: {project} (owner: {project.owner})')

# Create a workflow
workflow, _ = Workflow.objects.get_or_create(project=project, name='Admin Workflow')
print(f'Workflow: {workflow}')

# Create 15 tasks for pagination testing
for i in range(1, 16):
    task, created = Task.objects.get_or_create(
        workflow=workflow,
        title=f'Task {i}',
        defaults={'description': f'Description for task {i}', 'status': 'todo'}
    )
    if created:
        print(f'Created: {task}')

total_tasks = Task.objects.filter(workflow__project__owner=admin).count()
print(f'\nTotal tasks for admin: {total_tasks}')
