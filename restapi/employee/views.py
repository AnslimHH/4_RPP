from django.shortcuts import render, redirect
import requests
# Create your views here.
TEMPLATE = 'employee'
def index(request):
    context = {}

    response_type = requests.get('http://127.0.0.1:8000/api/orders/')
    if response_type.headers['Content-Type'] == 'application/json':
        context.update({"orders": response_type.json()})

    return render(request, TEMPLATE + '/index.html', context=context)



