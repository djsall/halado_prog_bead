from django.shortcuts import render

# example post data - TODO: Convert to DICT ARRAY so multiple posts can be viewed
posts_data = {
	"title": "yeah, here we go",
	"content": "Fuck you",
	"created-at": "2020-06-09"
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
		posts_data
	)


# submit post view
def submitpost(request):
	return render(
		request,
		'submit_post.html'
	)


