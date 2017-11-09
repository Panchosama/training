from django import forms
from .models import Entrenamiento, Piloto, Curso
#from django.contrib.admin import widgets  

# Formulario Entrenamiento
class EntrenamientoForm(forms.ModelForm):
	class Meta:
		model = Entrenamiento
		fields = ("curso", "fecha", "piloto")

# Formulario Piloto		
class PilotoForm(forms.ModelForm):
	class Meta:
		model = Piloto
		fields = ('nombre','licencia')

# Formulario Curso
class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = ('nombre', 'vigencia')