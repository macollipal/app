from enum import unique
from django.db import models

from base.models import ClaseModelo


class Categoria(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripción de la categoría', unique=True)

    def __str__(self) :
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural="Categorias"


#SubCategoria ******************************************************************************
class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la categoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural="Sub Categorias"
        unique_together = ('categoria', 'descripcion')

    #UM ******************************************************************************
class UM(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='descrip de la U Medida', unique=True)

    def __str__(self) :
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UM, self).save()

    class Meta:
        verbose_name_plural="UM"


class Producto(ClaseModelo):
    codigo= models.CharField(max_length=20, unique=True)
    nombre= models.CharField(max_length=20, unique=True)
    codigo_barra = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    saldo = models.IntegerField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)
    cant_max = models.IntegerField(default=0)
    cant_min = models.IntegerField(default=0)
    u_medida = models.ForeignKey(UM, on_delete=models.CASCADE)
    #subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self) :
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural="Productos"
        unique_together =('id', 'codigo_barra')
        ordering = ["id", "codigo_barra"]

