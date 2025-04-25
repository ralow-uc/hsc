from django.contrib import admin

from .models import TipoUsuario,Usuario,Venta,Categoria,TipoProd,Marca,Modelo,Producto,Region,Comuna,Direccion,Detalle
# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Venta)
admin.site.register(Categoria)
admin.site.register(TipoProd)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Producto)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Detalle)


