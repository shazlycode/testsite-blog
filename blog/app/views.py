from django.shortcuts import render, get_object_or_404
from app .models import Post
from app .forms import CommentForm, RegisterForm
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
    
    
    
    
    context = {
        'title': 'التسجيل',
        'register_form': register_form,
    }
    return render(request, 'app/register.html', context)