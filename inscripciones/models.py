from django.db import models
from .validators import validar_vencimiento, validar_descto

class Profesor(models.Model):
    nombre_completo = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre_completo

class TipoCurso(models.TextChoices):
   INFANTIL = 'inf', 'Infantil'
   ADULTO = 'adt', 'Adulto' 

class Curso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=300)
    max_alumnos = models.IntegerField()
    precio_hora = models.DecimalField(decimal_places=2, max_digits=5)
    tipo = models.CharField(
        max_length=3,
        choices=TipoCurso.choices,
        default=TipoCurso.ADULTO
    )
    profesores = models.ManyToManyField(Profesor)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

class CursoProfesor(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Alumno(models.Model):
    nombre_completo = models.CharField(max_length=150, unique=True)
    activo = models.BooleanField(blank=False, default=False)
    vencimiento = models.DateField(validators=[validar_vencimiento,])
    horas_dia = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')])
    dias_semana = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')])
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    precio_hora = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True, editable=False)
    monto_descto = models.DecimalField(decimal_places=2, max_digits=5, validators=[validar_descto,])
    monto_total = models.DecimalField(decimal_places=2, max_digits=10, default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def calcular_precio_hora(self):
        # Calcula el precio hora basado en el curso del alumno
        return self.curso.precio_hora if self.curso.precio_hora is not None else 0
    
    def calcular_monto_total(self):
        return (self.horas_dia * self.dias_semana * self.calcular_precio_hora() * 4) - self.monto_descto
    
    
    def save(self, *args, **kwargs):
        self.precio_hora = self.calcular_precio_hora()  # Actualiza el precio hora antes de guardar
        self.monto_total = self.calcular_monto_total()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre_completo
