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
	path('', views.index, name='index'),
	path('viewposts', views.viewposts, name='viewposts'),
	path('submitpost', views.submitpost, name='submitpost'),
	path('signup', views.signup, name='signup'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('home', views.home, name='home')
]

# static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)