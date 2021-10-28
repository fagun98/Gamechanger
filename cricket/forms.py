from django import forms
from .models import formation


class formationForm(forms.ModelForm):
    class Meta:
        model = formation
        fields = [
                'type_of_match',
                'no_of_batsmen',
                'right_batsmen',
                'left_batsmen',
                'no_of_Pacer',
                'pacer_right',
                'pacer_left',
                'spinner_right', 
                'spinner_left',
                'no_of_wicketkeeper',  
        ]