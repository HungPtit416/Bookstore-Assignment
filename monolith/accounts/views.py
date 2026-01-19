from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Customer

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        Customer.objects.create(name=name, email=email, password=password)
        return redirect('accounts:login')
    return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            customer = Customer.objects.get(email=email)
            if check_password(password, customer.password):
                request.session['customer_id'] = customer.id  # Lưu session đơn giản
                return redirect('books:catalog')
        except:
            pass
    return render(request, 'accounts/login.html')