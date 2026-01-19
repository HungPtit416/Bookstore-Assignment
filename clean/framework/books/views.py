from django.http import JsonResponse
from infrastructure.repositories import BookRepository
from usecases.book_usecases import GetAllBooks, GetBook

book_repo = BookRepository()

def list_books(request):
    use_case = GetAllBooks(book_repo)
    books = use_case.execute()
    return JsonResponse({
        'books': [{'id': b.id, 'title': b.title, 'author': b.author, 
                   'price': float(b.price), 'stock': b.stock} for b in books]
    })

def get_book(request, book_id):
    use_case = GetBook(book_repo)
    book = use_case.execute(book_id)
    if not book:
        return JsonResponse({'error': 'Not found'}, status=404)
    return JsonResponse({'id': book.id, 'title': book.title, 
                        'author': book.author, 'price': float(book.price), 
                        'stock': book.stock})