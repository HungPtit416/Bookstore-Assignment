class AddToCart:
    def __init__(self, cart_repo, book_repo):
        self.cart_repo = cart_repo
        self.book_repo = book_repo
    
    def execute(self, customer_id, book_id, quantity):
        # Kiểm tra sách tồn tại
        book = self.book_repo.find_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        
        if book.stock < quantity:
            raise ValueError("Insufficient stock")
        
        # Lấy hoặc tạo cart
        cart = self.cart_repo.get_or_create(customer_id)
        
        # Thêm item vào cart
        return self.cart_repo.add_item(cart.id, book_id, quantity)

class ViewCart:
    def __init__(self, cart_repo):
        self.cart_repo = cart_repo
    
    def execute(self, customer_id):
        return self.cart_repo.get_items(customer_id)