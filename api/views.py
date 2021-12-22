from django.http.response import HttpResponse, JsonResponse
#from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework.renderers import JSONRenderer

from book.models import Book
from .serializers import BookSerializer
#from api import serializers
from django.http import HttpResponse

def BookAPIView(request):
    queryset = Book.objects.all()
    print(queryset)
    serial = BookSerializer(queryset,many=True)
   # print(serializer_class)
   #return JsonResponse(serial.data,safe=False)

    json_data =JSONRenderer().render(serial.data)
    return HttpResponse(json_data,content_type='application/json')

'''def BookAPIView(request):
    queryset = Book.objects.all()
    print(queryset)
    serializer = BookSerializer(queryset,many=True)
   # print(serializer_class)
   return JsonResponse(serializer.data,safe=False)'''