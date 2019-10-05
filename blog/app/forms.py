from django import forms
from app.models import Post, Comment, Profile
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
    password1= forms.CharField(widget=forms.PasswordInput(),label='كلمة المرور',min_length=8)
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تأكيد كلمة المرور', min_length=8)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        
        
    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('اسم المستخدم موجود مسبقا')
        return cd['username']
    
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['password2']
    
    
    
class LoginForm(forms.ModelForm):
    username= forms.CharField(max_length=100, label='اسم المستخدم')
    password= forms.CharField(widget=forms.PasswordInput(), label='كلمة المرور')
    class Meta:
        model= User
        fields= ('username', 'password')
        
        
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='الاسم الأول')
    last_name = forms.CharField(label='الاسم الأخير')
    email = forms.EmailField(label='البريد الإلكتروني')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)       
#class ProfileUpdateForm(forms.ModelForm):
#    first_name = forms.CharField(max_length=100, label='الاسم الاول')
#    last_name = forms.CharField(max_length=100, label='الاسم الاخير')
#    email = forms.EmailField(label='البريد الالكتروني')
#    class Meta:
#        model = User
#        fields = ('first_name', 'last_name', 'email')
 #        
#class ImageUpdateForm(forms.ModelForm):
#    class Meta:
#        model = Profile
#        fields = ('image', )





class NewPost(forms.ModelForm):
    post_name= forms.CharField(max_length=500, label='عنوان التدوينة')
    post_body= forms.TextInput()
    class Meta:
        model= Post
        fields=('post_name', 'post_body',)