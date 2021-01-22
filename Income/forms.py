from django import forms

class CreateItem(forms.Form):
    income=forms.IntegerField()
    description=forms.CharField(max_length=500)


class Calculate(forms.Form):
    fixed_cost=forms.IntegerField()
    variable_cost=forms.IntegerField()
    actual_sales=forms.IntegerField()
    selling_price=forms.IntegerField()
