from django.shortcuts import render

# example post data - TODO: Convert to DICT ARRAY so multiple posts can be viewed
post_data = {
	"title": "yeah, here we go",
	"content": "Fuck you",
	"created": "2020-06-09"
}
posts = {
	"post_1": post_data,
	"post_2": post_data
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
		posts
	)


# submit post view
def submitpost(request):
	return render(
		request,
		'submit_post.html'
	)
#signup form
def signup(request):
	return render(
		request,
		'signup.html'
	)
