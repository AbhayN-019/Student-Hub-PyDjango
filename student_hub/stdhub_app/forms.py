from django import forms
from stdhub_app.models import Student

class StudentForm(forms.ModelForm):
    class Meta :
        model = Student
        fields = "__all__"
        widgets = {
            'title' : forms.TextInput(attrs={
                'placeholder' : 'Enter book title'
            }),
            'author' : forms.TextInput(attrs={
                'placeholder' : 'Enter author name'
            }),
            'published_date' : forms.DateInput(attrs={
                'type' : 'data'
            }),
            'description' : forms.Textarea(attrs={
                'placeholder' : 'Short description...',
                'rows' : 4
            }),
        }