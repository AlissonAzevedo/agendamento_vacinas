from django.contrib import admin
from .models import Paciente, Enfermeiro, Vacina, Local, Cidade, Estado, Vacinacao


# Register your models here.

admin.site.register(Paciente)
admin.site.register(Local)
admin.site.register(Enfermeiro)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Vacina)
admin.site.register(Vacinacao)