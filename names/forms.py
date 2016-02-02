__author__ = 'yaseen'

from django.forms import ModelForm
from django.forms import TextInput
from models import Name


class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'enter name'})
