# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Piloto, Curso, Entrenamiento

# Create your views here.
def piloto_list(request):
	pilotos=Piloto.objects.filter(activo=True).order_by('nombre')
	return render(request, 'training/piloto_list.html',{'pilotos':pilotos})

# def curso_list(request):
# 	cursos=Curso.objects.get()
# 	return render(request, 'training/curso_list.html',{'cursos':cursos})