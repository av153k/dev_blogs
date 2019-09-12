from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class new_user_form(UserCreationForm):
    first_name = forms.CharField(max_length=70)
    second_name = forms.CharField(max_length=70)
    username = forms.CharField(max_length=70)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields =  ("first_name", "second_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(new_user_form, self).save(commit = False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
        
class user_profile_form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("avatar",)

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        return avatar