
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
def archive(request):
	return render(request, 'archive.html', {"posts": Article.objects.all()})

# Create your views here.
