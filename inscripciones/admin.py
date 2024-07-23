from django.contrib import admin
from .models import Curso
from .models import Profesor
from .models import Alumno

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Alumno)