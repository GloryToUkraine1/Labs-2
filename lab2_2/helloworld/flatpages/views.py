from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
#def home(request):
	#return HttpResponse("Привет")
	#return HttpResponse()
def home(request):
	return render(request, 'static_handler.html', {})
