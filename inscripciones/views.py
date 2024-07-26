from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics
from .models import Curso, Alumno
from .serializers import CursoSerializer
from .forms import AlumnoForm
from rest_framework.decorators import api_view

def index(request):
    return HttpResponse("Bienvenido al módulo de inscripciones")

def cursos(request):
    post_nombre = request.POST.get("nombre")
    if post_nombre:
        q = Curso(nombre=post_nombre)
        q.save()
        
    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        cursos = Curso.objects.filter(nombre__contains=filtro_nombre)
    else:
        cursos = Curso.objects.all()
    return render(request, "form_categorias.html", {"cursos": cursos})

def alumnoFormView(request):
    form = AlumnoForm()
    alumno = None
    id_alumno = request.GET.get("id")
    if id_alumno:
        alumno = get_object_or_404(Alumno, id=id_alumno)
        form = AlumnoForm(instance=alumno)
        
    if request.method == "POST":
        if alumno:
            form = AlumnoForm(request.POST, instance=alumno)
        else:
            form = AlumnoForm(request.POST)
            
    if form.is_valid():
        form.save()
        
    return render(request, "form_alumno.html", {"form": form})

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('nombre')
    serializer_class = CursoSerializer
    
class CursoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Curso.objects.all().order_by('nombre')
    serializer_class = CursoSerializer
    
@api_view(['GET'])
def curso_count(request):
    """
    Cuenta la cantidad de cursos
    """
    
    try:
        cantidad = Curso.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )