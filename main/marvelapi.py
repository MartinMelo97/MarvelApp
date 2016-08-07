import requests	
import hashlib

class PachuMarvel(object):
	'''Clase del repo que consume la API de Marvel desde Pachuca'''
	def __init__(self, public_key='a894cc5c33cc66d0ed473368134b55e9', private_key='aa60a539d58291d44af640d7c02164ca8ecf4d6e'):
		self.public_key = public_key
		self.private_key = private_key
		ts = "1"
		self.ha = hashlib.md5((ts+self.private_key+self.public_key).encode()).hexdigest()
		self.url = "http://gateway.marvel.com/v1/public/"
		self.nombre = ""
		self.comic = "Star Wars"
		self.description = ""
		self.img = ""
		self.personaje = None
		self.comics = None

	def get_personaje(self, ide = 1009351):
		'''Este metodo obtiene toda la informacion del personaje desde el API de Marvel'''
		#self.nombre = input("Ingresa el personaje del que quieres saber su info: ")
		try:
			self.personaje = requests.get(
				self.url +'characters',
				params ={
				'apikey': self.public_key,
				'ts': '1',
				'hash': self.ha,
				'id': ide,
				}).json()
			self.nombre = self.personaje['data']['results'][0]['name']
			self.description = self.personaje['data']['results'][0]['description']
			self.img = self.personaje['data']['results'][0]['thumbnail']['path'] + '.'+'jpg'
			print("Asi joder, ya guarde tu personaje maldito friki")
		except Exception(e):
			print(e)

	def get_response(self):
		'''Este metodo solo puede ser llamado despues de get_personaje'''
		try:
			print(self.personaje)
		except:
			print("Algo pasó y no se que es x_x")

	def get_id(self):
		''' Este metodo setea el id del personaje'''
		try:
			self.ide = self.personaje['data']['results'][0]['id']
			print(self.ide)
		except:
			print('llama primero get_personaje sonso')

	def get_comics(self):
		'''Este obtiene la informacion de comics'''
		try:
			self.comics = requests.get(
				self.url + 'comics',
				params = {
				'apikey': self.public_key,
				'ts': '1',
				'hash': self.ha,
				'title': self.comic
				}).json()
			self.description = self.comics['data']['results'][0]['description']
			self.img = self.comics['data']['results'][0]['thumbnail']['path'] + '.' + 'jpg'
			print("Yeeeah")
			#print(self.comics)
			print(self.description)
			print(self.img)
		except:
			print("Mierda :(")

#ts = "1"
#public_key = "a894cc5c33cc66d0ed473368134b55e9"
#private_key = "aa60a539d58291d44af640d7c02164ca8ecf4d6e"
#ha = hashlib.md5((ts+private_key+public_key).encode()).hexdigest()
#url = "http://gateway.marvel.com/v1/public/"
'''
per = ""
while per != "q" or per != "Q":
	per = input("Ingresa el personaje que deseas obtener su info: ")
	personaje = requests.get(url+"characters",params = {"apikey":public_key, "ts": ts, "hash": ha, "name": per}).json()

	name = personaje['data']['results'][0]['name']
	description = personaje['data']['results'][0]['description']
	img = personaje['data']['results'][0]['thumbnail']['path'] +"."+ personaje['data']['results'][0]['thumbnail']['extension']
	print("Nombre: " + name)b
	print("Descripcion: " + description)'''
