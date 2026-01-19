from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Book

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            price=data['price'],
            stock=data['stock']
        )
        return JsonResponse({'message': 'Book created', 'id': book.id})

def get_books(request):
    return JsonResponse(list(Book.objects.values()), safe=False)
