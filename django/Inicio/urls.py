from django.urls import path
from .views import (
    iniciar,
    iniciar_sesion,
    inicio,
    registrar_m,
    registrarse,
    addprod,
    eliminarProducto,
    menuadmin,
    mostrarTeclado,
    mostrarMic,
    mostrarMouse,
    mostrarGrafica,
    mostrarRam,
    mostrarProcesador,
    perfilusuario,
    edicionProducto,
    editarProducto,
    recuperar_contrasena,
    cerrar_sesion,
    detalleProducto,
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Pagina iniciar/ Solo carga pagina
    path("iniciar/", iniciar, name="iniciar"),
    # Valida usuario / Aqui tenemos las consultas
    path("iniciarsesion/", iniciar_sesion, name="iniciarsesion"),
    # La pagina principal
    path("", inicio, name="inicio"),
    path("registrar/", registrar_m, name="registrar"),
    path("registrarse/", registrarse, name="registrarse"),
    # Pag agregar producto
    path("agregar/", addprod, name="agregarprod"),
    # modificar un producto
    path("eliminarProducto/<idProducto>", eliminarProducto, name="eliminarProducto"),
    # Pag menu admin
    path("menuadmin/", menuadmin, name="menu_admin"),
    # Mostrar productos
    path("teclados/", mostrarTeclado, name="mostrarTeclado"),
    path("microfonos/", mostrarMic, name="mostrarMic"),
    path("mouses/", mostrarMouse, name="mostrarMouse"),
    path("graficas/", mostrarGrafica, name="mostrarGrafica"),
    path("rams/", mostrarRam, name="mostrarRam"),
    path("procesadores/", mostrarProcesador, name="mostrarProcesador"),
    path("producto/<int:id>", detalleProducto, name="detalleProducto"),
    # Usuario
    path("miperfil/", perfilusuario, name="miperfil"),
    path("edicionProducto/<idProducto>", edicionProducto, name="edicionProducto"),
    path("editarProducto/<idProducto>", editarProducto, name="editarProducto"),
    path("recuperar", recuperar_contrasena, name="recuperar"),
    path("cerrar/", cerrar_sesion, name="cerrar"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
