from django.shortcuts import render, redirect
from .models import Cart, CartItem
from books.models import Book

def add_to_cart(request, book_id):
    if 'customer_id' not in request.session:
        return redirect('accounts:login')
    customer_id = request.session['customer_id']
    book = Book.objects.get(id=book_id)
    cart, created = Cart.objects.get_or_create(customer_id=customer_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('books:catalog')

def view_cart(request):
    if 'customer_id' not in request.session:
        return redirect('accounts:login')
    cart = Cart.objects.get(customer_id=request.session['customer_id'])
    items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart/view_cart.html', {'items': items})