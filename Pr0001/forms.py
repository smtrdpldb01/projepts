from django import forms
from .models import Pr0001

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Pr0001
        fields=["title1","title2","title3","title4","title5","title6","title7","title8","content"]