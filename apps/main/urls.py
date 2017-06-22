from django.conf.urls import url
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^confirm/(?P<id>\d+)$', views.confirm, name='confirm'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),
]
