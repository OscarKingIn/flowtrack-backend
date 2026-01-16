from django.contrib.auth.models import User
from projects.models import Project

# Create User A
user_a, created = User.objects.get_or_create(username='userA', defaults={'email': 'usera@test.com'})
if created:
    user_a.set_password('password123')
    user_a.save()
    print('✓ Created User A')
else:
    print('✓ User A already exists')

# Create User B
user_b, created = User.objects.get_or_create(username='userB', defaults={'email': 'userb@test.com'})
if created:
    user_b.set_password('password123')
    user_b.save()
    print('✓ Created User B')
else:
    print('✓ User B already exists')

# Create a project for User A
project, created = Project.objects.get_or_create(
    name='User A Project',
    defaults={'description': 'Project owned by User A', 'owner': user_a}
)
if created:
    print('✓ Created Project for User A')
else:
    print('✓ Project already exists')

print('\n--- Permission Test Scenario ---')
print('User A: username=userA, password=password123')
print('User B: username=userB, password=password123')
print(f'Project ID {project.id}: Owner=userA')
print('\nTest commands:')
print('1. Login as User A → GET /api/projects/{id}/ → Should succeed ✓')
print('2. Login as User B → GET /api/projects/{id}/ → Should fail with 403 ✗')
