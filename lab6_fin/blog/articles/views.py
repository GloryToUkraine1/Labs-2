
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import RegisterForm
from django.contrib import admin
from django.contrib.auth import login
from .models import LoginForm
from django.http import HttpResponseRedirect

def archive(request):
	return render(request, 'archive.html', {"posts": Article.objects.all()})
	
def get_article(request, article_id):
	try:
		post = Article.objects.get(id = article_id)
		return render(request, 'article.html', {"post": post})
	except Article.DoesNotExist:
		raise Http404

def create_post(request):
	if request.user.is_authenticated:
		if request.method == "POST":
		# обработать данные формы, если метод POST
			form = {'text': request.POST["text"], 'title': request.POST["title"]}
			# в словаре form будет храниться информация, введенная пользователем
			if form["text"] and form["title"]:
			# если поля заполнены без ошибок
				title = form["title"]
				#Article.objects.filter(title=title).exists() возвращает тру если нашла хоть одну запись из формы
				if not Article.objects.filter(title=title).exists():
					article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
					return redirect('get_article', article_id=article.id)
				else:
					form['errors'] = "Введите уникальное название"
					return render(request, 'create_post.html', {'form': form})
			# перейти на страницу поста
			else:
			# если введенные данные некорректны
				form['errors'] = "Не все поля заполнены"
				return render(request, 'create_post.html', {'form': form})
		else:
			# просто вернуть страницу с формой, если метод GET
			return render(request, 'create_post.html', {})
	else:
		raise Http404

#def register(request):
	#return render(request, 'register.html', {})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, email=user.email, password=raw_password)
            login(request, user)
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Create your views here.
def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.get_user():
                login(request, form.get_user())
                return HttpResponseRedirect('../../archive/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
