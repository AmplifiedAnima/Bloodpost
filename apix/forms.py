from email.mime import image
from socket import fromshare
from django.forms import ModelForm
from django import forms
from . models import Comment, Post, Profile
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields =['username','email']
        
    
class ChangeProfile(ModelForm):
    class Meta:
        model = Profile
        fields=['image',]

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('user','name','image','body')
        widgets= {
        'user': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
    }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields= ('body',)



