from interfaces.repositories import ICustomerRepository, IBookRepository, ICartRepository
from domain.entities import Customer, Book, Cart, CartItem
from django.contrib.auth.hashers import make_password, check_password

class CustomerRepository(ICustomerRepository):
    def create(self, customer):
        from framework.accounts.models import CustomerModel
        customer_model = CustomerModel.objects.create(
            name=customer.name,
            email=customer.email,
            password=make_password(customer.password)
        )
        customer.id = customer_model.id
        return customer
    
    def find_by_email(self, email):
        from framework.accounts.models import CustomerModel
        try:
            c = CustomerModel.objects.get(email=email)
            return Customer(id=c.id, name=c.name, email=c.email, password=c.password)
        except CustomerModel.DoesNotExist:
            return None

class BookRepository(IBookRepository):
    def get_all(self):
        from framework.books.models import BookModel
        books = BookModel.objects.all()
        return [Book(id=b.id, title=b.title, author=b.author, 
                     price=b.price, stock=b.stock) for b in books]
    
    def find_by_id(self, book_id):
        from framework.books.models import BookModel
        try:
            b = BookModel.objects.get(id=book_id)
            return Book(id=b.id, title=b.title, author=b.author, 
                       price=b.price, stock=b.stock)
        except BookModel.DoesNotExist:
            return None

class CartRepository(ICartRepository):
    def get_or_create(self, customer_id):
        from framework.cart.models import CartModel
        cart_model, _ = CartModel.objects.get_or_create(customer_id=customer_id)
        return Cart(id=cart_model.id, customer_id=cart_model.customer_id, 
                   created_at=cart_model.created_at)
    
    def add_item(self, cart_id, book_id, quantity):
        from framework.cart.models import CartItemModel
        item, created = CartItemModel.objects.get_or_create(
            cart_id=cart_id, book_id=book_id,
            defaults={'quantity': quantity}
        )
        if not created:
            item.quantity += quantity
            item.save()
        return CartItem(id=item.id, cart_id=item.cart_id, 
                       book_id=item.book_id, quantity=item.quantity)
    
    def get_items(self, customer_id):
        from framework.cart.models import CartModel, CartItemModel
        try:
            cart = CartModel.objects.get(customer_id=customer_id)
            items = CartItemModel.objects.filter(cart=cart).select_related('book')
            return [CartItem(id=i.id, cart_id=i.cart_id, 
                           book_id=i.book_id, quantity=i.quantity) for i in items]
        except CartModel.DoesNotExist:
            return []