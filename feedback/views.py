from django.shortcuts import render
from . import forms
# Create your views here.

def feedbackviews(request):
    form = forms.FeedbackForm()
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            print('forms validation sucessfull and printing information')
            print('Name: ',form.cleaned_data['name'])
            print('Roll Number: ',form.cleaned_data['rollnum'])
            print('Email: ', form.cleaned_data['email'])
            print('feedback: ',form.cleaned_data['feedback'])
    return render(request,'feedbackapp/feedback.html', {'form':form})