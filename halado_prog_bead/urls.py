from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from halado_prog_bead import views


urlpatterns = [
	path('admin/', admin.site.urls),
]

# include index
urlpatterns += [
	#index
	path('', views.index, name='index'),
	#posts
	path('viewposts', views.viewposts, name='viewposts'),
	#submit post
	path('submitpost', views.submitpost, name='submitpost'),
	#signup
	path('signup', views.signup, name='signup'),
	#login
	path('accounts/', include('django.contrib.auth.urls')),
	#home redirect for login
	path('home', views.home, name='home')
]

# static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)