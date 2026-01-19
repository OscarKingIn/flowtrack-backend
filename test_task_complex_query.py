#!/usr/bin/env python
"""Test combined filtering, searching, ordering, and pagination on tasks API"""

import os
import sys
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowtrack.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

client = Client()

print('\n=== TASKS COMPLEX QUERY TEST ===\n')

# Get admin user JWT token
response = client.post('/api/token/', {'username': 'admin', 'password': 'admin123'}, content_type='application/json')
if response.status_code == 200:
    token = response.json()['access']
    print('✓ Got JWT token for admin user')
else:
    print('✗ Failed to get token')
    sys.exit(1)

headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

# Test combined query
print('\n--- Tasks with status=doing, search=api, ordering=-created_at, page=1 ---')
response = client.get('/api/tasks/?status=doing&search=api&ordering=-created_at&page=1', **headers)
if response.status_code == 200:
    data = response.json()
    print(f'Status: 200 OK')
    print(f'Count: {data.get("count")} total results')
    print(f'Results on this page: {len(data.get("results", []))}')
    if data.get('results'):
        print(f'\nFirst result: {json.dumps(data["results"][0], indent=2)}')
else:
    print(f'Status: {response.status_code}')

print('\n=== COMPLEX QUERY TEST COMPLETE ===\n')
