class RegisterCustomer:
    def __init__(self, customer_repo):
        self.customer_repo = customer_repo
    
    def execute(self, name, email, password):
        from domain.entities import Customer
        customer = Customer(name=name, email=email, password=password)
        return self.customer_repo.create(customer)

class LoginCustomer:
    def __init__(self, customer_repo):
        self.customer_repo = customer_repo
    
    def execute(self, email, password):
        return self.customer_repo.find_by_email(email)