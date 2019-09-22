from django.shortcuts import render
from app .models import Post

# Create your views here.
def index(request):
    posts= Post.objects.all()
    context= {
        'title': "الرئيسيـــة",
        'posts': posts,
    }
    
    return render(request, 'app/index.html', context)