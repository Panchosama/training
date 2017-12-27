# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^$' , views.index),
	url(r'^pilotos/$' , views.piloto_list, name = 'piloto_list'),
	url(r'^piloto/(?P<pk>[0-9]+)/$' , views.piloto_detail, name = 'piloto_detail'),
	url(r'^cursos/$' , views.curso_list, name='curso_list'),
	url(r'^entrenamiento/new/$' , views.entrenamiento_new, name = 'entrenamiento_new'),
	url(r'^piloto/new/$' , views.piloto_new, name = 'piloto_new'),
	url(r'^curso/new/$' , views.curso_new, name = 'curso_new'),
	url(r'^curso/(?P<pk>[0-9]+)/$' , views.curso_detail, name = 'curso_detail'),
	url(r'^piloto/(?P<pk>[0-9]+)/edit/$' , views.piloto_edit, name = 'piloto_edit'),
	url(r'^entrenamiento/(?P<pk>[0-9]+)/edit/$' , views.entrenamiento_edit, name = 'entrenamiento_edit'),
	url(r'^curso/(?P<pk>[0-9]+)/edit/$' , views.curso_edit, name = 'curso_edit'),
]