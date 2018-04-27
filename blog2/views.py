from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
	return render(request, 'blog2/index.html')

def hello(request):
	return render(request, 'blog2/hello.html')