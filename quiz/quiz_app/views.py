from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the quiz index.")
	
def login(request):
	return HttpResponse("Login")
	
def register(request):
	return HttpResponse("Register")
	
def quiz(request):
	return HttpResponse("Quiz")
	
def results(request):
	return HttpResponse("Login")