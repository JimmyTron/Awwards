# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from django.forms import ModelForm
# from django.contrib.auth.models import User

# class RegisterForm(UserCreationForm):
#     username = forms.CharField(max_length=50, label='username', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
#     email = forms.EmailField(max_length=50, label='email', widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}))
#     password1 = forms.CharField(max_length=50, label='password', widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))
#     password2 = forms.CharField(max_length=50, label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']



from django import forms
from .models import Project,Profile,Rating

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['username','post_date','design','usability','creativity','content','overall_score','avatar',]
        widgets={
        'technologies':forms.CheckboxSelectMultiple(),
        'categories':forms.CheckboxSelectMultiple(),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['overall_score','profile','project']