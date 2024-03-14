from django import forms
from Connection.models import Studentinfo


class StudentForm(forms.Form):
    name = forms.CharField(label='Enter your name', max_length=50, required=True)
    age = forms.IntegerField(label='Enter your age', required=True, min_value=18)
    check = forms.BooleanField(label='Do you really want to join this organisation?', required=False)
    category = forms.ChoiceField(choices=[('Student', 'Student'), ('parent', 'parent'),
                                          ('teacher', 'teacher'), ('board-master', 'board-master')], required=False)


class StudentinfoForm(forms.ModelForm):
    class Meta:
        model = Studentinfo
        fields = ['FirstName', 'LastName', 'Age', 'BirthDate']
