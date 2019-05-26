# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import forms
from django.contrib.auth import login, authenticate

class Article(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s: %s" % (self.author.username, self.title)

	def get_excerpt(self):
		return self.text[:140] + "..." if len(self.text) > 140 else self.text

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email',)
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Имя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Имя пользователя и пароль не подходят')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None
