from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Cart, CartItem

@csrf_exempt
def create_cart(request):
    data = json.loads(request.body)
    cart = Cart.objects.create(customer_id=data['customer_id'])
    return JsonResponse({'cart_id': cart.id})

@csrf_exempt
def add_item(request):
    data = json.loads(request.body)
    CartItem.objects.create(
        cart_id=data['cart_id'],
        book_id=data['book_id'],
        quantity=data['quantity']
    )
    return JsonResponse({'message': 'Item added'})
