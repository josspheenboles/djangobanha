from django import forms
from track.models import Track
from .models import Trainee
class TraineeFormModel(forms.ModelForm):
    class Meta:
        model=Trainee
        fields='__all__'#['name','email']
        exclude=['Active',]
        label={            'name'               :'Full name'}
        widget={'name':forms.TextInput()}


class TraineeForm(forms.Form):
    trname=forms.CharField(required=True,max_length=100,
                         widget=forms.TextInput(
                             attrs={'text-color':'red','border':'1px'}
                         ))
    tremail=forms.CharField(required=True,widget=forms.EmailInput())
    trtrack=forms.ChoiceField(choices=[(track.id,track.name) for track in Track.getalltracks()])
    trimg=forms.ImageField(required=True)
    # password=forms.CharField(required=True,widget=forms.PasswordInput())