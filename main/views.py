from django.shortcuts import render
from django.views.generic import View
from .marvelapi import PachuMarvel
'''import requests	
import hashlib
ts = "1"
public_key = "a894cc5c33cc66d0ed473368134b55e9"
private_key = "aa60a539d58291d44af640d7c02164ca8ecf4d6e"
ha = hashlib.md5((ts+private_key+public_key).encode()).hexdigest()
url = "http://gateway.marvel.com/v1/public/"'''

'''class Welcome(View):
	def get(self, request):
		template_name = "home.html"
		personaje = Marvel()
		name = personaje['data']['results'][0]['name']
		description = personaje['data']['results'][0]['description']
		img = personaje['data']['results'][0]['thumbnail']['path'] +"."+ personaje['data']['results'][0]['thumbnail']['extension']
		return render(request,template_name, {'name': name, 'desc': description, 'img': img})

def Marvel():
	import requests	
	import hashlib
	ts = "1"
	public_key = "a894cc5c33cc66d0ed473368134b55e9"
	private_key = "aa60a539d58291d44af640d7c02164ca8ecf4d6e"
	ha = hashlib.md5((ts+private_key+public_key).encode()).hexdigest()
	url = "http://gateway.marvel.com/v1/public/"
	template_name = "home.html"
	personaje = requests.get(url+"characters",params = {"apikey":public_key, "ts": ts, "hash": ha, "name": "Hulk"}).json()
	return personaje
'''


class Welcome(View):
	def get(self, request, ide):
		template_name = "home.html"
		#q = request.GET.get('search')
		#if q == None:
		#	q = 'Hulk'
		personaje = PachuMarvel()
		personaje.get_personaje(ide)
		name = personaje.nombre
		description = personaje.description
		img = personaje.img
		return render(request, template_name, {'name': name, 'desc': description, 'img': img})

class Comics(View):
	def get(self, request):
		template_name = "comics.html"
		comicss = PachuMarvel()
		comicss.get_comics()
		title = comicss.comic
		description = comicss.description
		img = comicss.img
		return render(request, template_name, {'name': title, 'desc': description, 'img': img})
		
class SelectSuper(View):
	def get(self,request):
		template_name = "personaje.html"
		return render(request, template_name)