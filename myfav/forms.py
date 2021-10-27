from django.forms import ModelForm
from .models import Myfav

class MyfavForm(ModelForm):
    class Meta:
        model = Myfav
        fields = ['name', 'author_or_creator', 'genre', 'image', 'description']