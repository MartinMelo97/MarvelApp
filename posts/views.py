from django.shortcuts import render
from django.views.generic import View
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm

class ListView(View):
	def get(self, request):
		
		template_name = 'blog.html'
		user = User.objects.get(username='tecmartinmelo')
		entradas=user.blog_posts.all()
		context = {
			'posts':entradas
			
		}
		return render(request,template_name,context)

class DetailView(View):
	def get(self, request, slug):
		template_name = "detalle.html"
		post = Post.objects.get(slug=slug)
		context = {
		'post':post
		}
		return render(request, template_name, context)

class NuevoPost(View):
	def get(self, request):
		form = PostForm()
		template_name = "nuevo.html"
		context = {'form':form}
		return render(request, template_name, context)

	def post(self,request):
		pass
		form = PostForm(request.POST)
		form.save()
		template_name = 'nuevo.html'
		context = {
			'guardado': True,
		}
		return render(request, template_name, context)
		#titulo = request.POST.get('Titulo')
		#cuerpo = request.POST.get('cuerpo')
		#post = Post()
		#try: 
		#	post.autor = request.user
		#except:
		#	pass
		#post.titulo = titulo
		#post.cuerpo = cuerpo
		#post.save()

		#template_name = "nuevo.html"
		#context = {'guardado':True}

		#return render(request, template_name, context)