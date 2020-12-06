from django.shortcuts import render
from django.http import HttpRequest;
from django.template import Context

# example post data - TODO: Convert to DICT ARRAY so multiple posts can be viewed
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
def signup(request):
	return render(
		request,
		'registration/signup.html'
	)
