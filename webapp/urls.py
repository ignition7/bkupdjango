from django.conf.urls import url, include

from webapp import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
