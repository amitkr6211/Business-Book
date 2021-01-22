from django import forms    
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,Extra
class UserRegisterForm(UserCreationForm):
    email =forms.EmailField()
    class Meta:
        model = User
        #it will be saved in this model 
        fields = ['username','email','password1','password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ExtraForm(forms.ModelForm):
    # age=forms.IntegerField()
    # business=forms.CharField(max_length=500)
    class Meta:
        model = Extra
        fields=['age','business']

   

