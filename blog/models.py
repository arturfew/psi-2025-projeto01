from django.db import models

class Info(models.Model):
    info = models.CharField(max_length=200)
    sobre = models.TextField
    data_publicacao = models.DateTimeField(auto_now=True)


class Post(models.Model):  # Corrigido: models.Model e nome com maiúscula (boas práticas)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='posts/')  # Corrigido: ImageField
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo  # Corrigido: self, não slef


# Create your models here.
