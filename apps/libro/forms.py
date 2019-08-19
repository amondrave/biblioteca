from django import forms as fm
from .models import Autor

class AutorForm(fm.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellido','nacionalidad','descripcion']
