from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r"cursos", views.CursoViewSet)

urlpatterns = [
    #path('cursos/', views.cursos, name='cursos'),
    #path('alumnos/', views.alumnos, name='alumnos'),
    #path('',include(router.urls))
    path('cursos/', views.CursoCreateView.as_view()),
    path('cursos/cantidad/', views.curso_count),
]
