from django import forms
from .models import Relics

class RelicsForm(forms.ModelForm):
    class Meta:
        model = Relics
        fields = "__all__"
    
    mod_type = forms.ChoiceField(
        choices = Relics.objects.values('mod_type').distinct(),
        label = 'relic_mod_type'
    )