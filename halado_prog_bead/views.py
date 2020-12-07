from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import models
from halado_prog_bead.models import Post
from datetime import datetime

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
		{'posts': Post.objects.all()}
	)


# submit post view
@login_required
def submitpost(request):
	if request.method == 'GET':
		return render(
			request,
			'submit_post.html'
		)
	elif request.method == 'POST':
		Post.objects.create(
			Text=request.POST['post_body'],
			Author=request.user,
			Title=request.POST['post_title'],
			Time=datetime.now()
			).save();
		return render(
		request,
		'view_posts.html',
		{'posts': Post.objects.all()}
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
