from django.shortcuts import render, get_object_or_404, redirect
from app .models import Post
from app .forms import CommentForm, RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    posts= Post.objects.all()
    context= {
        'title': "الرئيسيـــة",
        'posts': posts,
    }
    
    return render(request, 'app/index.html', context)

def post_details(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    # comments = post.comment.filter(active=True)
    comments = post.comment.all()
    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form= CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment =comment_form.save(commit=False)
            new_comment.post= post
            new_comment.save()
            comment_form = CommentForm()
        
        
    else:
        comment_form = CommentForm()
        
    
    
    context = {
        'title': 'تفاصيل التدوينة',
        'post': post ,
        'comments': comments,
        'comment_form': comment_form, 
        
        
    }
    return render(request, 'app/post_details.html', context)




def register(request):
    register_form= RegisterForm()
    if request.method == 'POST':
        register_form= RegisterForm(request.POST)
        if register_form.is_valid():
            new_user= register_form.save(commit=False)
            password= register_form.cleaned_data['password1']
            username= register_form.cleaned_data['username']
            new_user.set_password(password)
            new_user.save()
            messages.success(request,'تهانينا {} لقد تم تسجيلك بنجاح'.format(username))
            return redirect('index')
      
    else:
        register_form= RegisterForm()
     
    context = {
        'title': 'التسجيل',
        'register_form': register_form,
    }
    return render(request, 'app/register.html', context)


def login_user(request):
    
    if request.method == 'POST':
        login_form= LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'مرحبا {} لقد تم تسجيل الدخول بنجاح'.format(username))
            return redirect('index')
        else:
            messages.warning(request, 'هناك خطا في اسم المستخدم او كلمة المرور')
            
            
        
        
    else:
        login_form= LoginForm()
        
    
    
    
    context= {
        'title': 'تسجيل الدخول',
        'login_form':login_form,
    }
    return render(request, 'app/login.html', context)



def logout_user(request):
    logout(request)
    
    context= {
        'title':'تسجيل الخروج'
    }
    return render(request, 'app/logout.html', context)
