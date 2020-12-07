from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

article_data = {
	"title": "yeah, here we go",
	"content": "Fuck you",
	"created_at": "2020-06-09",
	"created_by": "gergo"
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
@login_required
def submitpost(request):
	return render(
		request,
		'submit_post.html'
	)


# redirect view for login
def home(request):
	return HttpResponseRedirect('/')


# signup form
def signup(request):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('index')
	return render(request, 'registration/signup.html', {'form': form})
