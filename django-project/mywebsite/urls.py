from django.contrib import admin
from django.urls import include, path


from . import views
from django.http import HttpResponse


urlpatterns = [
    path('', views.indexb),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('polls/', include('polls.urls'))
    
]



