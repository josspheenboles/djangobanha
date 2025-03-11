from django import forms
from track.models import Track
class TraineeForm(forms.Form):

    name=forms.CharField(max_length=100,label='Full Name',required=True)
    email=forms.EmailField(required=True)
    track=forms.ChoiceField(choices=[(track.id,track.name)
                                     for track in Track.getalltracks()])

