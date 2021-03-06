from django.db import models
from usuario.models import Profile , datos_prestamo_manejado_por_staff

# Create your models here.

  
class Autor(models.Model):

	nombre = models.CharField(max_length=200 , blank= False , null = False)
	apellido = models.CharField(max_length=200 , blank=False , null=False)
	descripcion= models.TextField(blank=False , null=False)
	estado = models.BooleanField('estado' , default=True)
	create = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now= True)

	def __str__(self): 
		return self.nombre

class Libro(models.Model):
	
	titulo= models.CharField(max_length=200 , blank= False , null = False)
	
	cantidad_existente= models.IntegerField() 
	autor_id= models.ManyToManyField(Autor , blank=True )
	creado = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now= True)
	estado = models.BooleanField('estado' , default=True)


	def __str__(self):

		return '{}'.format(self.titulo)



class Prestamo(models.Model):

	libro_id= models.ManyToManyField(Libro)
	user_id =  models.ForeignKey(datos_prestamo_manejado_por_staff, on_delete=models.CASCADE)
	created= models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now= True)
	libro_prestado =models.BooleanField(default=True)
	libro_entregado=models.BooleanField(default=False)
	entregado_date= models.DateTimeField(null=True, blank=True)	


class reservation(models.Model):

	
	user_id =  models.ForeignKey(Profile, on_delete=models.CASCADE)

	titulo_libro= models.CharField(max_length=200 , blank= False , null = False)
	
	cantidad_solicitada= models.IntegerField() 
	descripcion= models.TextField(blank=False , null=False)
	autor_libro= models.CharField(max_length=200 , blank= False , null = True)
	creado = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now= True)
	estado = models.BooleanField('estado' , default=True)


	def __str__(self):
		
		return '{} , {}'.format(self.titulo_libro ,self.user_id.email)








	