from django import forms
from .models import *

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

