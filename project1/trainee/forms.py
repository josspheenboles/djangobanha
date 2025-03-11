from gc import enable

from django import forms
class TraineeForm(forms.Form):
    name=forms.CharField(max_length=100,label='Full Name',required=True)
    email=forms.EmailField(required=True)
    track=forms.ChoiceField(choices=(('1','python'),))

