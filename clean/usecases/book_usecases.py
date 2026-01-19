class GetAllBooks:
    def __init__(self, book_repo):
        self.book_repo = book_repo
    
    def execute(self):
        return self.book_repo.get_all()

class GetBook:
    def __init__(self, book_repo):
        self.book_repo = book_repo
    
    def execute(self, book_id):
        return self.book_repo.find_by_id(book_id)