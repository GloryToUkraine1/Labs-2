
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth import authenticate

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

# Create your views here.
