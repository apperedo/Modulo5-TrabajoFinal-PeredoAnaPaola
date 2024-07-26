from rest_framework import serializers
from .models import Curso, Alumno

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"
        
class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"
        
class ReporteAlumnoSerializer(serializers.Serializer):
    cantidad = serializers.ImageField()
    alumno = AlumnoSerializer(many=True)
    