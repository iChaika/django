from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

def detail(request, post_id):
    blog = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/fullstory.html', {'blog': blog})