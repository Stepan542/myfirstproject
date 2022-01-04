from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('Hello! NICE COOCKIES')

def home(request):
	return render(request, 'home.html', {'MyLife':'Good'}) 
