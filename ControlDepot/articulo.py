#-*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models


class Articulo(models.Model):
#    class Meta:
    cod_articulo = models.primary_key #CharField(max_length=100)
    categoria = models.IntegerField
    f_venc = models.DateTimeField 
    f_ingreso = models.DateTimeField
    time_stock = models.IntegerField
    count_stock = models.IntegerField
    nombre_articulo = models.CharField(max_length=200)
 #   id_provedor = models.CharField(max_length=100)


    def Articulo(self, nombre, cantidad, vencimieto, categoria):
		self.cod_articulo = self.categoria 
		self.f_venc = vencimiento
		self.f_ingreso = timezone.now
		self.time_stock = 30
		self.count_stock = self.count_stock + cantidad
		self.nombre_articulo = nombre 
		self.categoria = categoria

    def getCodArticulo(self):
		return self.cod_articulo 

    def getFechaVenc(self):
		return self.f_venc 

    def getFechaIngreso(self):
		return self.f_ingreso 

    def getTimeStock(self):
		return self.time_stock 

    def getCountStock(self):
		return self.cod_articulo 

    def getNameArticulo(self):
		return self.nombre_articulo 

  #  def getIdProvedor(self):
#		return self.id_provedor 

		
    def setCountStock(self,cantidad):
		self.count_stock = self.count_stock + cantidad
    def setNameArticulo(self, name):
		self.nombre_articulo = name	
