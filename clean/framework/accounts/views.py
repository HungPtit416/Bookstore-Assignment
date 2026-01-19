from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from infrastructure.repositories import CustomerRepository
from usecases.customer_usecases import RegisterCustomer, LoginCustomer
from django.contrib.auth.hashers import check_password

customer_repo = CustomerRepository()

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        use_case = RegisterCustomer(customer_repo)
        
        # Kiểm tra email tồn tại
        if customer_repo.find_by_email(data['email']):
            return JsonResponse({'error': 'Email exists'}, status=400)
        
        customer = use_case.execute(data['name'], data['email'], data['password'])
        return JsonResponse({'message': 'Success', 'id': customer.id}, status=201)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        use_case = LoginCustomer(customer_repo)
        customer = use_case.execute(data['email'], data['password'])
        
        if not customer or not check_password(data['password'], customer.password):
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
        
        return JsonResponse({'message': 'Login success', 'id': customer.id})