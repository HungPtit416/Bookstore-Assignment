import os
import django
from decimal import Decimal
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

# Import models
from accounts.models import Customer
from books.models import Book
from cart.models import Cart, CartItem

# Clear existing data if needed (optional, comment out if you don't want to delete)
# Customer.objects.all().delete()
# Book.objects.all().delete()
# Cart.objects.all().delete()
# CartItem.objects.all().delete()

# Create sample Customers
# Note: Passwords are stored in plaintext as per your model (not recommended for production)
customer1 = Customer.objects.create(
    name='John Doe',
    email='john@example.com',
    password='pass123'
)

customer2 = Customer.objects.create(
    name='Jane Smith',
    email='jane@example.com',
    password='pass456'
)

# Create sample Books
book1 = Book.objects.create(
    title='The Great Gatsby',
    author='F. Scott Fitzgerald',
    price=Decimal('10.99'),
    stock=100
)

book2 = Book.objects.create(
    title='To Kill a Mockingbird',
    author='Harper Lee',
    price=Decimal('15.50'),
    stock=50
)

book3 = Book.objects.create(
    title='1984',
    author='George Orwell',
    price=Decimal('12.75'),
    stock=75
)

# Create Carts for Customers (OneToOne, so only one per customer)
cart1 = Cart.objects.create(customer=customer1)

cart2 = Cart.objects.create(customer=customer2)

# Create CartItems for cart1
CartItem.objects.create(
    cart=cart1,
    book=book1,
    quantity=2
)

CartItem.objects.create(
    cart=cart1,
    book=book2,
    quantity=1
)

# Create CartItems for cart2
CartItem.objects.create(
    cart=cart2,
    book=book2,
    quantity=3
)

CartItem.objects.create(
    cart=cart2,
    book=book3,
    quantity=1
)

print("Sample data inserted successfully!")