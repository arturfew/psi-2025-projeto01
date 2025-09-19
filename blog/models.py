from django.db import models

class Info(models.Model):
    info = models.CharField(max_length=200)
    sobre = models.TextField(blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info


class Post(models.Model):  
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='posts/')  
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo 


# Create your models here.
