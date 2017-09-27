# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Piloto, Curso, Entrenamiento

# Register your models here.
admin.site.register(Piloto)
admin.site.register(Curso)
admin.site.register(Entrenamiento)