from abc import ABC, abstractmethod

class ICustomerRepository(ABC):
    @abstractmethod
    def create(self, customer):
        pass
    
    @abstractmethod
    def find_by_email(self, email):
        pass

class IBookRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def find_by_id(self, book_id):
        pass

class ICartRepository(ABC):
    @abstractmethod
    def get_or_create(self, customer_id):
        pass
    
    @abstractmethod
    def add_item(self, cart_id, book_id, quantity):
        pass
    
    @abstractmethod
    def get_items(self, customer_id):
        pass