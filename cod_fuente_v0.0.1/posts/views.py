from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.
def index(request):
    # if request.user.is_authenticated:
    #     data = {
    #         'title': "Lista completa",
    #     }
    # else:
    #     data = {
    #         'title': "Lista simple",
    #     }
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
    })

def posts_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post,})

def posts_create(request):
    return HttpResponse("<h1>Crear!</h1>")

def posts_update(request):
    return HttpResponse("<h1>Act!</h1>")

def posts_delete(request):
    return HttpResponse("<h1>Borrar!</h1>")