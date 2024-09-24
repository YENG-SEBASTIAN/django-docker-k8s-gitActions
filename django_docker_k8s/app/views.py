from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello, World! Johnnnn')
    
    def post(self, request):
        return HttpResponse('Hello, World! POST request received.')
    
    def put(self, request):
        return HttpResponse('Hello, World! PUT request received.')
    
    def delete(self, request):
        return HttpResponse('Hello, World! DELETE request received.')
    