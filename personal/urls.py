from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^webapp/', include('webapp.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='index'),
]
