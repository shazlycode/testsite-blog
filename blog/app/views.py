from django.shortcuts import render, get_object_or_404, redirect
from app .models import Post
from app .forms import CommentForm, RegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm, NewPost
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth. decorators import login_required
from django.db.models import Q


# Create your views here.
def index(request):
    posts= Post.objects.all()
    title_search_box= request.GET.get('title_search')
    auther_search_box= request.GET.get('auther_search')
    title_content_search_box= request.GET.get('title_content_search')
    if title_search_box != '' and title_search_box is not None:
        posts= posts.filter(post_name__icontains=title_search_box)
    if auther_search_box != '' and auther_search_box is not None:
        posts=posts.filter(auther__username__icontains=auther_search_box)
    elif title_content_search_box !='' and title_content_search_box is not None:
        posts=posts.filter(Q(post_name__icontains=title_content_search_box)|Q(post_body__icontains=title_content_search_box))
        
        
        
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
            return redirect('login')
      
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
            return redirect('profile')
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

@login_required(login_url='login')
def profile(request):
    posts= Post.objects.filter(auther=request.user)
    
    
    
    
    context = {
        'title': 'الملف الشخصي',
        'posts': posts,
    }
    return render(request, 'app/profile.html', context)

@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'تم تحديث الملف الشخصي.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'تعديل الملف الشخصي',
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'app/profile_update.html', context)


# def profile_update(request):
    
#     if request.method == "POST":
        
#         user_update= ProfileUpdateForm(request.POST, instance = request.user)
#         profile_update = ImageUpdateForm(request.POST, request.FILES)
#         if user_update.is_valid and profile_update.is_valid:
#             user_update.save()
#             profile_update.save(commit=True)
#     else:
#         user_update= ProfileUpdateForm(instance=request.user)
#         profile_update= ImageUpdateForm(instance= request.user.profile)
        
            
    
    
    
#     context = {
#         'title': 'تعديل الملف الشخصي',
#         'user_update': user_update,
#         'profile_update': profile_update,
        
#     }
#     return render (request,'app/profile_update.html', context)


def new_post(request):
    
    if request.method=='POST':
        newpost= NewPost(request.POST)
        if newpost.is_valid:
            new= newpost.save(commit=False)
            new.auther = request.user
            new.save()
            return redirect('/')
            
            
    
    else:
        newpost= NewPost()
        
    
    context ={
        'title':'اضافة تدوينة جديدة',
        'newpost':newpost,
        
    }
    return render(request, 'app/new_post.html', context)


def update_post(request, post_id):
    note= get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        newpost=NewPost(request.POST, instance= note)
        if newpost.is_valid():
            new= newpost.save(commit=False)
            new.auther= request.user
            new.save()
            return redirect('/')
    else:
        newpost=NewPost()
    context={
        'title': 'تحرير تدوينة',
        'newpost': newpost,
        'post':note,
        
    }
    return render(request, 'app/update_post.html', context)

def delete_post(request,post_id):
    post= get_object_or_404(Post, pk=post_id)
    post.delete()
    
    return redirect('/')
    