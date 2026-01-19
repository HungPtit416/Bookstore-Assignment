from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from infrastructure.repositories import CartRepository, BookRepository
from usecases.cart_usecases import AddToCart, ViewCart

cart_repo = CartRepository()
book_repo = BookRepository()

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        use_case = AddToCart(cart_repo, book_repo)
        try:
            item = use_case.execute(
                data['customer_id'], 
                data['book_id'], 
                data.get('quantity', 1)
            )
            return JsonResponse({'message': 'Added', 'id': item.id}, status=201)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)

def view_cart(request, customer_id):
    use_case = ViewCart(cart_repo)
    items = use_case.execute(customer_id)
    return JsonResponse({
        'items': [{'id': i.id, 'book_id': i.book_id, 
                   'quantity': i.quantity} for i in items]
    })