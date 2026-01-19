#!/usr/bin/env python
"""Test ordering tasks by -created_at (descending)"""

import os
import sys
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowtrack.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

client = Client()

print('\n=== TASK ORDERING TEST ===\n')

# Get admin user JWT token
response = client.post('/api/token/', {'username': 'admin', 'password': 'admin123'}, content_type='application/json')
if response.status_code == 200:
    token = response.json()['access']
    print('✓ Got JWT token for admin user')
else:
    print('✗ Failed to get token')
    sys.exit(1)

headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

# Test ordering=-created_at
print('\n--- Tasks ordered by -created_at ---')
response = client.get('/api/tasks/?ordering=-created_at', **headers)
if response.status_code == 200:
    data = response.json()
    print(f'Status: 200 OK')
    print(f'Count: {data.get("count")} total results')
    print(f'Results on this page: {len(data.get("results", []))}')
    if data.get('results'):
        print(f'\nFirst task (most recent): {data["results"][0]}')
else:
    print(f'Status: {response.status_code}')

print('\n=== ORDERING TEST COMPLETE ===\n')
