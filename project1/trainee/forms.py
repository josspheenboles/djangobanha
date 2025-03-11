from django import forms
class TraineeForm(forms.Form):
    name=forms.CharField(max_length=100,required=True)
