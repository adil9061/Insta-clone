from django import forms
from logbook.models import profile,Post

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class Editprofile(forms.ModelForm):
    class Meta:
        model=profile
        exclude=('user',)
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fileds=['image','caption',]
        exclude=('user',)



