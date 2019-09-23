from django import forms
from app.models import Post, Comment
from django.contrib.auth.models import User 



class CommentForm(forms.ModelForm):
    
    
    class Meta:
        model = Comment
        fields = ('name','email','comment_body' )
        
        
        
class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='اسم المستخدم')
    first_name = forms.CharField(max_length=100, label='الاسم الاول')
    last_name = forms.CharField(max_length=100, label='الاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني')
    password1= forms.CharField(widget=forms.PasswordInput(),label='كلمة المرور')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تأكيد كلمة المرور')
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2','email')