from django import forms

class TipoAtividadeForm(forms.ModelForm):

    class Meta:
        widgets = {
            'faixa': forms.TextInput(attrs={'size': 20}),
            'texto_explicativo': forms.TextInput(attrs={'size': 20}),
            'duracao_faixa': forms.NumberInput(attrs={'size': 7}),
            'duracao_faixa_presencial': forms.NumberInput(attrs={'size': 7}),
        }