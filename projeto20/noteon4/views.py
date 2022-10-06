from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 as error404
from  .models import usuarios, anotacoes 
from . import urls

def viewtindex(request):
	return render(request,'index.html')

def viewtlogin(request):
	return render(request,'tlogin.html')

def viewtregistro(request):
	return render(request,'tregistro.html')

def viewtpainel(request,id):
	try:
		usuario=error404(usuarios,pk=id)
		nota=anotacoes.objects.all()
		return render(request,'tpainel.html',{'USUARIO':usuario,'NOTA':nota})
	except:
		return HttpResponse("Ocorreu um Erro Fatal - Contate o Suporte (ERROR:003)")

def viewtvernota(request,id,id2):
	try:
		usuario=usuarios.objects.get(pk=id)	
		nota=anotacoes.objects.get(pk=id2)
		return render(request,'tvernota.html',{'USUARIO':usuario,'NOTA':nota})
	except:
		return HttpResponse("Ocorreu um Erro Fatal - Contate o Suporte (ERROR:005)")


def viewtperfil(request,id):
	try:
		usuario=usuarios.objects.get(pk=id)	
		return render(request,'tperfil.html',{'USUARIO':usuario})
	except:
		return HttpResponse("Ocorreu um Erro Fatal - Contate o Suporte (ERROR:007)")


def defbtnregistro(request):
	if request.method=="POST":
		email=request.POST.get('email')
		bdemails=usuarios.objects.filter(email=email)
		
		if not bdemails:
			nome=request.POST.get('nome')
			sobrenome=request.POST.get('sobrenome')
			email=request.POST.get('email')
			senha=request.POST.get('senha')
			nvusario=usuarios(nome=nome,sobrenome=sobrenome,senha=senha,email=email)
			nvusario.save()
			return render(request,'tlogin.html',{'kepEmail':email,'kepSenha':senha})
		else:
			nome=request.POST.get('nome')
			sobrenome=request.POST.get('sobrenome')
			email=request.POST.get('email')
			senha=request.POST.get('senha')
			return render(request,'tregistro.html',{'kepEmail':email,'kepSenha':senha,'EmailAlert':"Email já cadastrado",'kepNome':nome,'kepSobrenome':sobrenome})
	else:
		return HttpResponse("Ocorreu um Erro Fatal - Contate o Suporte (ERROR:001)")


def defbtnlogin(request):
	if request.method=="POST":
		email=request.POST.get('email')
		senha=request.POST.get('senha')
		try:
			bdemails=error404(usuarios,email=email)
		except:
			return render(request,'tlogin.html',{'EmailAlert':"Email Não Encontrado",'kepSenha':senha,'kepEmail':email})
		if bdemails.senha == senha:

			userId=usuarios.objects.get(email=email)
			nota=anotacoes.objects.all()
			return render(request,'tpainel.html',{'USUARIO':userId,'NOTA':nota})
		else:
			return render(request,'tlogin.html',{'SenhaAlert':"Senha Errada",'kepSenha':senha,'kepEmail':email})
	
	return HttpResponse("Ocorreu um Erro Fatal - Contate o Suporte (ERROR:002)")


def defbtnnvnota(request,id):
	usuario=usuarios.objects.get(pk=id)
	return render(request,'tnvnota.html',{'USUARIO':usuario})


def defsavenvnota(request,id):
	if request.method=="POST":
		titulo=request.POST.get('titulo')
		subtitulo=request.POST.get('subtitulo')
		cor=request.POST.get('cor')
		texto=request.POST.get('texto')
		nvnota=anotacoes(titulo=titulo,subtitulo=subtitulo,cor=cor,texto=texto)
		nvnota.save()
		usuario=usuarios.objects.get(pk=id)
		nota=anotacoes.objects.all()
		return render(request,'tpainel.html',{'USUARIO':usuario,'NOTA':nota})
	else: 
		return HttpResponse("Ocorreu um Erro Fatal - Contate o Suporte (ERROR:004)")

def defeditar(request,id,id2):
	if request.method=="POST":
			nota=anotacoes.objects.get(pk=id2)
			nota.subtitulo=request.POST.get('subtitulo')
			nota.texto=request.POST.get('texto')
			nota.cor=request.POST.get('cor')
			nota.titulo=request.POST.get('titulo')
			nota.save()
			
			usuario=usuarios.objects.get(pk=id)
			notas=anotacoes.objects.all()
			return render(request,'tpainel.html',{'USUARIO':usuario, 'NOTA':notas})
	else:
		return HttpResponse("Ocorreu um Erro Fatal - Contate o Suporte (ERROR:006)")


def defeditarperfil (request,id):
	if request.method=="POST":
		usuario=usuarios.objects.get(pk=id)
		usuario.nome=request.POST.get('nome')
		usuario.sobrenome=request.POST.get('sobrenome')
		usuario.email=request.POST.get('email')
		usuario.senha=request.POST.get('senha')
		usuario.save()

		return render(request,'tperfil.html',{'USUARIO':usuario})
	else:
		return HttpResponse("Ocorreu um Erro Fatal - Contate o Suporte (ERROR:006)")		

def defdeletar(request,id,id2):	
	try:	
		nota=anotacoes.objects.get(pk=id2)
		try:
			nota.delete()
		except:
			usuario=usuarios.objects.get(pk=id)	
			notas=anotacoes.objects.all()
			return render(request,'tpainel.html',{'USUARIO':usuario,'NOTA':notas})

		usuario=usuarios.objects.get(pk=id)	
		notas=anotacoes.objects.all()
		return render(request,'tpainel.html',{'USUARIO':usuario,'NOTA':notas})
	except:
		try:
			usuario=usuarios.objects.get(pk=id)	
			notas=anotacoes.objects.all()
			return render(request,'tpainel.html',{'USUARIO':usuario,'NOTA':notas})
		except:
			return HttpResponse("Ocorreu um Erro Fatal - Contate o Suporte (ERROR:009)")
