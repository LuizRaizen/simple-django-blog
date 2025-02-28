from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario


def lista_posts(request):
    """Uma lista com todas as postagens feitas no Blog."""

    posts = Post.objects.order_by("-data_pub")
    return render(request, "blog/index.html", {'posts': posts})


def detalhe_post(request, post_id):
    """Uma página que mostra um post detalhadamente."""

    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        autor = request.POST.get('autor')
        conteudo = request.POST.get('conteudo')
        Comentario.objects.create(post=post, autor=autor, conteudo=conteudo)
    
    return render(request, 'blog/post.html', {'post': post})
