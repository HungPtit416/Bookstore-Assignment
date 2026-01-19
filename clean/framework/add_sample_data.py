import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from books.models import BookModel
from accounts.models import CustomerModel
from django.contrib.auth.hashers import make_password

# Xóa dữ liệu cũ (nếu có)
BookModel.objects.all().delete()
CustomerModel.objects.all().delete()

# Thêm Books
print("Adding books...")
BookModel.objects.create(
    title='Clean Code',
    author='Robert C. Martin',
    price=45.99,
    stock=10
)

BookModel.objects.create(
    title='Design Patterns',
    author='Gang of Four',
    price=55.00,
    stock=8
)

BookModel.objects.create(
    title='The Pragmatic Programmer',
    author='Andrew Hunt',
    price=42.50,
    stock=15
)

# Thêm Customers
print("Adding customers...")
CustomerModel.objects.create(
    name='John Doe',
    email='john@test.com',
    password=make_password('password123')
)

CustomerModel.objects.create(
    name='Jane Smith',
    email='jane@test.com',
    password=make_password('password123')
)

print("✓ Sample data added successfully!")
print("\nBooks added: 3")
print("Customers added: 2")
print("\nTest credentials:")
print("- Email: john@test.com | Password: password123")
print("- Email: jane@test.com | Password: password123")