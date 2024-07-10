from django.forms import ModelForm
from .models import Curso

class FormularioCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ['colegio', 'nivel_curso', 'cantidad_alumnos', 'servicio', 'destino', 'fecha_viaje', 'monto_depositado', 'id_cliente']

class EditarFormularioCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ['colegio', 'nivel_curso', 'cantidad_alumnos', 'servicio', 'destino', 'id_cliente']