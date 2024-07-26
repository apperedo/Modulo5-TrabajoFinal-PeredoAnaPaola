from rest_framework import serializers
from .models import Curso, Alumno, Profesor

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"
        
class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"
        
class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = "__all__"
        
class ReporteCursosSerializer(serializers.Serializer):
    cantidad = serializers.ImageField()
    cursos = CursoSerializer(many=True)
    