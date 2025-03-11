from django import forms
from track.models import Track
from .models import Trainee
class Traineeformmodel(forms.ModelForm):
    class Meta:
        model=Trainee



class TraineeForm(forms.Form):

    name=forms.CharField(max_length=100,label='Full Name',required=True)
    email=forms.EmailField(required=True)
    track=forms.ChoiceField(choices=[(track.id,track.name)
                                     for track in Track.getalltracks()])

    languages = forms.MultipleChoiceField(label='Languages',choices=((1,'ar'),(2,'eng')),
                                          widget=forms.CheckboxSelectMultiple)
    password=forms.CharField(widget=forms.HiddenInput)
    image=forms.FileField()