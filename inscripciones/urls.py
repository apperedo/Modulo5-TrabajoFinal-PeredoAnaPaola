from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r"cursos", views.CursoViewSet)
router.register(r"alumnos", views.AlumnoViewSet)
router.register(r"profesor", views.ProfesorViewSet)

urlpatterns = [
    path('cursos/', views.CursoCreateView.as_view()),
    path('alumnos/', views.AlumnoCreateView.as_view()),
    path('cursos/', views.ProfesorCreateView.as_view()),
    path('cursos/cantidad/', views.curso_count),
    path('',include(router.urls))
]
