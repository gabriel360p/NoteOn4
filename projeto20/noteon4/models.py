from django.db import models

class usuarios(models.Model):
	nome=models.CharField(max_length=50)
	sobrenome=models.CharField(max_length=50)
	senha=models.CharField(max_length=50)
	email=models.EmailField()
	def __str__(self):
		return f'{self.nome},{self.sobrenome},{self.email},{self.senha}'

class anotacoes(models.Model):
	titulo=models.CharField(max_length=50)
	subtitulo=models.CharField(max_length=50)
	cor=models.CharField(max_length=50)
	texto=models.TextField()
	def __str__(self):
		return f'{self.titulo},{self.subtitulo},{self.cor},{self.texto}'

