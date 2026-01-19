#!/usr/bin/env python
"""Test pagination of tasks API"""

import os
import sys
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowtrack.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

client = Client()

print('\n=== PAGINATION TEST ===\n')

# Get admin user JWT token
response = client.post('/api/token/', {'username': 'admin', 'password': 'admin123'}, content_type='application/json')
if response.status_code == 200:
    token = response.json()['access']
    print('✓ Got JWT token for admin user')
else:
    print('✗ Failed to get token')
    sys.exit(1)

headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

# Test page 1
print('\n--- Page 1 ---')
response = client.get('/api/tasks/?page=1', **headers)
if response.status_code == 200:
    data = response.json()
    print(f'Status: 200 OK')
    print(f'Count: {data.get("count")} total results')
    print(f'Results on this page: {len(data.get("results", []))}')
    print(f'Next page: {data.get("next")}')
    print(f'Previous page: {data.get("previous")}')
    if data.get('results'):
        print(f'\nFirst task on page 1: {data["results"][0]}')
else:
    print(f'Status: {response.status_code}')

# Test page 2
print('\n--- Page 2 ---')
response = client.get('/api/tasks/?page=2', **headers)
if response.status_code == 200:
    data = response.json()
    print(f'Status: 200 OK')
    print(f'Count: {data.get("count")} total results')
    print(f'Results on this page: {len(data.get("results", []))}')
    print(f'Next page: {data.get("next")}')
    print(f'Previous page: {data.get("previous")}')
    if data.get('results'):
        print(f'\nFirst task on page 2: {data["results"][0]}')
else:
    print(f'Status: {response.status_code} (expected 404 if less than 10 results)')

print('\n=== PAGINATION TEST COMPLETE ===\n')
