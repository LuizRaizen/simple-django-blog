from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Uma postagem do Blog."""

    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna uma representação em string do modelo."""

        if len(self.titulo) > 50:
            return self.titulo[:50] + "..."
        else:
            return self.titulo
        

class Comentario(models.Model):
    """Um comentário em uma postagem específica."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna uma reprsentação em string do modelo."""

        if len(self.autor) > 50:
            return f"Comentário feito por {self.autor[:50]}..."
        else:
            return f"Comentário de {self.autor}"
