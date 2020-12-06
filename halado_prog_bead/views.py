from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpRequest;
from django.template import Context

# example post data - TODO: Convert to DICT ARRAY so multiple posts can be viewed
from .forms import SignUpForm

article_data = {
	"title": "yeah, here we go",
	"content": "Fuck you",
	"created": "2020-06-09"
}
articles = {
	"post_1": article_data,
	"post_2": article_data
}


# index view
def index(request):
	return render(
		request,
		'index.html',
	)


# posts view
def viewposts(request):
	return render(
		request,
		'view_posts.html',
		{'myDict': articles}
	)


# submit post view
def submitpost(request):
	return render(
		request,
		'submit_post.html'
	)


# signup form
# https://dev.to/coderasha/create-advanced-user-sign-up-view-in-django-step-by-step-k9m
def signup(request):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		user = form.save()
		user.refresh_from_db()
		user.profile.first_name = form.cleaned_data.get('first_name')
		user.profile.last_name = form.cleaned_data.get('last_name')
		user.profile.email = form.cleaned_data.get('email')
		user.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('index')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})

	return render(
		request,
		'registration/signup.html'
	)
