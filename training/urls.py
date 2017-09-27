from django.conf.urls import include, url
from . import views

urlpatterns =[
	url(r'^$', views.index),
	url(r'^pilotos/$', views.piloto_list),
	url(r'^piloto/(?P<pk>[0-9]+)/$', views.piloto_detail, name='piloto_detail'),
	url(r'^cursos/$', views.curso_list),
]