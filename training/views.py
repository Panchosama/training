# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Piloto, Curso, Entrenamiento

# Create your views here.
def index(request):
	return render(request, 'training/index.html',{})

def piloto_list(request):
	pilotos=Piloto.objects.filter(activo=True).order_by('nombre')
	return render(request, 'training/piloto_list.html',{'pilotos':pilotos})

def piloto_detail(request, pk):
	piloto = get_object_or_404(Piloto, pk=pk)
	cursos = Entrenamiento.objects.filter(piloto=pk).order_by('fecha')
	return render(request, 'training/piloto_detail.html',{'piloto':piloto, 'cursos':cursos})

def curso_list(request):
	cursos=Curso.objects.all().order_by('nombre')
	return render(request, 'training/curso_list.html',{'cursos':cursos})