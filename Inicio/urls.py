from django.urls import path
from .views import iniciar,iniciar_sesion, inicio, inicioadmin, registrar_m, registrarse, newProd,addprod,vistamod,eliminarProducto,menuadmin,micadmin,tecladoadmin,mouseAdmin,ramAdmin,graficaAdmin,procesadorAdmin,mostrarTeclado,teclado,mostrarMic,micro,mostrarMouse,mouse,mostrarGrafica,grafica,mostrarRam,ram,mostrarProcesador,procesador,carrito,perfilusuario,edicionProducto,editarProducto, mostrarperfil, modificarPerfil ,agregar_producto,eliminar_producto,restar_producto,limpiar_producto
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    #Pagina iniciar/ Solo carga pagina
    path('iniciar/',iniciar,name="iniciar"),
    
    #Valida usuario / Aqui tenemos las consultas
    #Sacamos datos de aqui d1
    path('iniciarsesion/',iniciar_sesion,name ="iniciarsesion"),

    # La pagina principal
    #Metemos datos aqui d1
    path('', inicio, name="inicio"),



    path('indexadmin',inicioadmin,name="indexadmin"),

    path('registrar/',registrar_m,name="registrar"),
    path('registrarse/',registrarse,name="registrarse"),
    #Pag agregar producto
    path('agregar2/',newProd,name ="addProd"),
    path('agregar/',addprod,name="agregarprod"),
    #modificar un producto
    path('modificar/',vistamod,name="modificar"),
    path('eliminarProducto/<idProducto>',eliminarProducto,name="eliminarProducto"),

    #Pag menu admin
    path ('menuadmin/',menuadmin,name="menu_admin"),

    path('micadmin/<id>',micadmin,name="micadmin"),
    path('tecladoadmin/<id>',tecladoadmin,name="tecladoadmin"),
    path('mouseAdmin/<id>',mouseAdmin,name="mouseAdmin"),
    path('ramAdmin/<id>',ramAdmin,name="ramAdmin"),
    path('graficaAdmin/<id>',graficaAdmin,name="graficaAdmin"),
    path('procesadorAdmin/<id>',procesadorAdmin,name="procesadorAdmin"),
    
    #Mostrar productos
    path('teclados/<id>',mostrarTeclado,name="teclados"),
    path('teclados/<idk>/<usuario>',teclado, name="teclado"),

    path('microfonos/<id>',mostrarMic, name="mostrarMic"),
    path('microfono/<idmic>/<usuario>',micro, name="micro"),

    path('mouses/<id>',mostrarMouse, name="mostrarMouse"),
    path('mouses/<idm>/<usuario>',mouse, name="mouse"),

    path('graficas/<id>',mostrarGrafica, name="mostrarGrafica"),
    path('graficas/<idg>/<usuario>',grafica, name="grafica"),

    path('rams/<id>',mostrarRam, name="mostrarRam"),
    path('rams/<idr>/<usuario>',ram, name="ram"),

    path('procesadores/<id>',mostrarProcesador, name="mostrarProcesador"),
    path('procesadores/<idp>/<usuario>',procesador, name="procesador"),


    #Carrito
    path('carrito/<id>',carrito, name="carrito"),
    path('agregar3/<int:idProducto>/<str:usuario>',agregar_producto,name="Add"),
    path('eliminar/<int:idProducto>/<str:usuario>',eliminar_producto,name="Del"),
    path('restar/<int:idProducto>/<str:usuario>',restar_producto,name="Sub"),
    path('limpiar/<str:usuario>',limpiar_producto,name="CLS"),
    #Usuario
    path('miperfil/<id>',perfilusuario, name="miperfil"),
    path ('mostrarperfil/<id>', mostrarperfil, name="mostrarperfil"),
    path ('modificarPerfil/<id>', modificarPerfil, name="modificarPerfil"),
    


    path('edicionProducto/<idProducto>', edicionProducto, name="edicionProducto"),
    path('editarProducto/<idProducto>', editarProducto, name="editarProducto"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)