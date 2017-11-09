# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Piloto, Curso, Entrenamiento
from .forms import EntrenamientoForm, PilotoForm, CursoForm

# Create your views here.
def index(request):
	entrenamientos = Entrenamiento.objects.all()
	return render(request, 'training/index.html',{'entrenamientos':entrenamientos})

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

def entrenamiento_new(request):
	if request.method == "POST":
		form = EntrenamientoForm(request.POST)
		if form.is_valid():
			entrenamiento = form.save(commit=False)
			entrenamiento.save()
			return redirect('/', pk=entrenamiento.pk)
	else:
		form = EntrenamientoForm()
	return render(request, 'training/entrenamiento_new.html', {'form':form})

def piloto_new(request):
	if request.method == "POST":
		form=PilotoForm(request.POST)
		if form.is_valid():
			curso = form.save(commit=False)
			curso.save()
			return redirect('piloto_detail', pk=piloto.pk)
	else:
		form= PilotoForm()
	return render(request, 'training/piloto_new.html', {'form':form})

def curso_new(request):
	if request.method == "POST":
		form=CursoForm(request.POST)
		if form.is_valid():
			curso = form.save(commit=False)
			curso.save()
			return redirect('curso_detail', pk=curso.pk)
	else:
		form = CursoForm()
	return render(request, 'training/curso_new.html', {'form':form})

def curso_detail(request, pk):
	curso = get_object_or_404(Curso, pk=pk)
	pilotos = Entrenamiento.objects.filter(curso=pk).order_by('fecha')
	return render(request, 'training/curso_detail.html',{'curso':curso, 'pilotos':pilotos})

def piloto_edit(request, pk):
        piloto = get_object_or_404(Piloto, pk=pk)
        if request.method == "POST":
            form = PilotoForm(request.POST, instance=piloto)
            if form.is_valid():
                piloto = form.save(commit=False)
                piloto.author = request.user
                piloto.save()
                return redirect('piloto_detail', pk=piloto.pk)
        else:
            form = PilotoForm(instance=piloto)
        return render(request, 'training/piloto_new.html', {'form': form})

def entrenamiento_edit(request, pk):
        entrenamiento = get_object_or_404(Entrenamiento, pk=pk)
        if request.method == "POST":
            form = EntrenamientoForm(request.POST, instance=entrenamiento)
            if form.is_valid():
                entrenamiento = form.save(commit=False)
                entrenamiento.author = request.user
                entrenamiento.save()
                return redirect('/', pk=entrenamiento.pk)
        else:
            form = EntrenamientoForm(instance=entrenamiento)
        return render(request, 'training/entrenamiento_new.html', {'form': form})