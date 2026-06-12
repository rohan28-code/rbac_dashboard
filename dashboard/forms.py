from django import forms
from .models import ProjectData

class ProjectDataForm(forms.ModelForm):

    class Meta:
        model = ProjectData
        fields = ['title', 'description']