from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Customer

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer = Customer.objects.create(
            name=data['name'],
            email=data['email'],
            password=data['password']
        )
        return JsonResponse({'message': 'Customer created', 'id': customer.id})

def get_customers(request):
    customers = list(Customer.objects.values())
    return JsonResponse(customers, safe=False)
