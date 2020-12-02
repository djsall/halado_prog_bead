from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(
			request,
			'index.html',
		)

def viewposts(request):
	return HttpResponse("this will display allll the posts")


from django.views import generic
