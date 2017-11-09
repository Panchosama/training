# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from dateutil.relativedelta import relativedelta

# Create your models here.
@python_2_unicode_compatible
class Piloto(models.Model):
	nombre=models.CharField(max_length=200)
	licencia=models.CharField(max_length=30)
	activo=models.BooleanField(default=True)

	def deshabilitar(self):
		self.activo=False
		self.save()

	def habilitar(self):
	 	self.activo=True
	 	self.save()

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Curso(models.Model):
	nombre=models.CharField(max_length=200)
	vigencia=models.IntegerField(help_text="En meses.")
	entrenamientos=models.ManyToManyField(Piloto, through="Entrenamiento")

	def __str__(self):
		return self.nombre

class Entrenamiento(models.Model):
	piloto=models.ForeignKey(Piloto)
	curso=models.ForeignKey(Curso)
	fecha=models.DateField()

	def vencimiento(self):
		vig = self.curso.vigencia
		venc= self.fecha + relativedelta(months=vig)
		return venc

	def alerta(self):
		dif=self.dif()
		if dif > timezone.timedelta(days=31):
			return "succ"
		elif dif <= timezone.timedelta(days=30):
			if dif > timezone.timedelta(days=1):
				return "warn"
			else:
				return "dang"

	def dif(self):
		hoy=timezone.now().date()
		ven=self.vencimiento()
		return (ven-hoy)

	# def ultimo(self):


	# def vigencia(self):
	# 	# Calculo el largo de la vigencia del curso, en días
	# 	year = timezone.timedelta(days=365)
	# 	vig = Curso.objects.filter(pk=self.curso).values('vigencia').get()
		
	# 	# Calculo fecha de vencimiento del curso
	# 	venc = self.fecha + relativedelta(months=vig['vigencia'])
	# 	hoy = timezone.now().date()

	# 	if (hoy-venc) <= timezone.timedelta(days=30):
	# 		return "Por vencer"
	# 	elif (hoy-venc) < timezone.timedelta(0):
	# 		return "Vencido por "+ str((hoy-venc)*-1) + u" días"
	# 	else:
	# 		return u"Al día"





