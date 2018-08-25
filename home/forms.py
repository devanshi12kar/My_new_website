from django import forms

from home.models import Musician
from home.models import Superheroes




class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name','last_name','instrument']

class SuperheroForm(forms.ModelForm):
    class Meta:
        model = Superheroes
        fields =['name','real_name','comics','powers']