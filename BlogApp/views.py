from django.shortcuts import render,get_object_or_404
from BlogApp.models import Post

# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all();
    return render(request,'BlogApp/post_list.html',{"post_list":post_list})

def post_detail_view(request, year,month,day,post):
    post=get_object_or_404(Post,slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day);
    return render(request, "BlogApp/post_detail.html",{'post':post})