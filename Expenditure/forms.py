from django import forms

class CreateItem(forms.Form):
    spending=forms.IntegerField()
    description=forms.CharField(max_length=500)