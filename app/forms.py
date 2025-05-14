import django.forms as forms
from .models import *
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LivroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'titulo',
            'autor',
            'editora',
            'genero',
            'preco',
            'data_pub',
            'status', 
            Submit('submit', 'Salvar')
        )
