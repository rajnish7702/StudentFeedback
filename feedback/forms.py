from django import forms
from django.core import validators

class FeedbackForm(forms.Form):
    name = forms.CharField()
    rollnum = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    def clean(self):
        print('Total Form validation')
        total_clead_data= super().clean()
        inputname = total_clead_data['name']
        if inputname[0].lower()!='d':
            raise forms.ValidationError('Name should start with D')
        inputroll = total_clead_data['rollnum']
        if inputroll<=0:
            raise forms.ValidationError('Roll Number')