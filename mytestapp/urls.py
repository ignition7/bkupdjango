
from django.conf.urls import url
from django.http import HttpResponse

from mytestapp import views


def work(request):
    return HttpResponse('Hi')


urlpatterns = [
    url(r'^test', views.myview),
]