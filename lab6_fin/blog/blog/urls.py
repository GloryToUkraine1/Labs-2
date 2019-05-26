"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles.views import archive
from articles.views import get_article
from articles.views import create_post
from articles.views import log_in
from articles.views import register

urlpatterns = [
    path('login/', log_in, name ='log_in'),
    path('register/', register, name ='register'),
    path('admin/article/new/', create_post, name ='create_post'),
	path('article/<int:article_id>/', get_article, name ='get_article'),
	path('archive/', archive, name ='archive'),
    path('admin/', admin.site.urls),
]
