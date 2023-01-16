from django.shortcuts import render, redirect
import requests

# Create your views here.
TEMPLATE = 'jewelryshop'

def index(request):
    context = {}

    if request.method == 'POST':
        secondname = str(request.POST.get('secondname', None))
        firstname = str(request.POST.get('firstname', None))
        patronymic = str(request.POST.get('patronymic', None))
        type = str(request.POST.get('type', None))
        address = str(request.POST.get('address', None))
        if secondname is not None and firstname is not None and type is not None and address is not None:
            requests.post('http://127.0.0.1:8000/api/orders/', json={'secondname': secondname,
                                                                     'firstname': firstname,
                                                                     'patronymic': patronymic,
                                                                     'type': type,
                                                                     'address': address})
            return redirect('index')
    return render(request, TEMPLATE + '/index.html', context=context)


