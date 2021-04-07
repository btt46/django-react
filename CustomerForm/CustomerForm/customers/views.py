from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .models import Customer
import json

# Create your views here.

@api_view(['GET','POST'])
def create_customer(request):
    if request.method == 'POST':
        print("request")
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        exist_customer = Customer.objects.filter(email=data['email']).count()

        if exist_customer == 0:
            name = data['name']
            tel = data['telephone']
            addr = data['address']
            email=data['email']
            print(name, tel, addr, email)
            new_customer = Customer.objects.create(name=name,telephone=tel,
                                    address=addr,email=email,nenkin_1_status='',nenkin_2_status='')
            new_customer.save()
            return Response(status=status.HTTP_201_CREATED)

    return HttpResponse(Customer.objects.all())