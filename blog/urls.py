"""Padrões de URL para o Blog."""
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # A página inicial mostrando uma lista de posts do Blog
    path('', views.lista_posts, name="lista_posts"),
    # A página de detalhes de um post específico
    path('post/<int:post_id>/', views.detalhe_post, name="detalhe_post")
]