from django.shortcuts import render, redirect
from utils.decorators import admin_requerido, login_requerido
from .models import (
    Usuario,
    Direccion,
    Comuna,
    Region,
    TipoUsuario,
    Producto,
    Marca,
    Categoria,
    TipoProd,
    Marca,
)
from django.contrib import messages
from .Carrito import Carrito
from django.conf import settings
import requests
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def inicio(request):
    return render(request, "Inicio/index.html")


def cerrar_sesion(request):
    request.session.flush()
    return redirect("inicio")


@admin_requerido
def inicioadmin(request):
    return render(request, "Inicio/index_admin.html")


def vistamod(request):

    return render(request, "Inicio/modificar_producto.html")


@admin_requerido
@csrf_exempt
def addprod(request):
    token = request.session.get("token")
    headers = {"Authorization": f"Bearer {token}"} if token else {}

    if request.method == "POST":
        nombre = request.POST.get("nomprod")
        tipoProd = request.POST.get("tipoprod")
        marca = request.POST.get("marcaprod")
        stock = request.POST.get("stockprod")
        desc = request.POST.get("descprod")
        precio = request.POST.get("precio")

        payload = {
            "nombreproducto": nombre,
            "tipoprod_id": int(tipoProd),
            "marca_id": int(marca),
            "stockprod": int(stock),
            "precioproducto": float(precio),
            "especificacionprod": desc,
        }
        
        print(payload)

        # files = {}
        # if request.FILES.get("imgprod"):
        #     files["imagenprod"] = request.FILES["imgprod"]

        try:
            response = requests.post(
                f"{settings.API_BUSINESS_URL}/productos",
                headers=headers,
                json=payload,
                # files=files,
                timeout=5,
            )
            if response.status_code in [200, 201]:
                messages.success(request, "¡Producto agregado correctamente!")
                return redirect("menu_admin")
            else:
                messages.error(request, f"Error {response.status_code}: No se pudo agregar el producto.")
        except Exception as e:
            messages.error(request, f"Error al conectar con la API: {e}")

    try:
        response_tipos = requests.get(f"{settings.API_BUSINESS_URL}/tipoproducto", timeout=5)
        tipoProd = response_tipos.json() if response_tipos.status_code == 200 else []

        response_marcas = requests.get(f"{settings.API_BUSINESS_URL}/marcas", timeout=5)
        marca = response_marcas.json() if response_marcas.status_code == 200 else []

    except Exception as e:
        tipoProd = []
        marca = []
        messages.error(request, f"Error al cargar tipos o marcas: {e}")

    contexto = {"tipoProd": tipoProd, "Marca": marca}
    return render(request, "Inicio/agregar_producto.html", contexto)


def iniciar(request):

    return render(request, "Inicio/inicio_sesion.html")


@admin_requerido
def menuadmin(request):
    return render(request, "Inicio/dashboard-admin.html")


def carrito(request, id):
    usuario = Usuario.objects.get(username=id)
    contexto = {"usuario": usuario}
    return render(request, "Inicio/carrito.html", contexto)


def perfilusuario(request):
    username = request.session.get("username")
    token = request.session.get("token")

    if not username or not token:
        messages.error(request, "Debes iniciar sesión para acceder al perfil.")
        return redirect("iniciar")

    headers = {"Authorization": f"Bearer {token}"}

    if request.method == "POST":
        nombre = request.POST.get("nomusu")
        apellido = request.POST.get("apepusu")
        email = request.POST.get("mailusu")
        direccion = request.POST.get("dirusu")
        region_id = request.POST.get("region")
        password = request.POST.get("password")

        payload_user = {
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "tipousuario_id": 2,
            "username": username,
            "contrasennia": password,
        }

        try:
            # Actualizar datos del usuario
            response_user = requests.put(
                f"{settings.API_AUTH_URL}/usuarios/{username}",
                headers=headers,
                json=payload_user,
                timeout=5,
            )

            # Obtener dirección actual
            response_dir = requests.get(
                f"{settings.API_BUSINESS_URL}/direcciones/usuario/{username}",
                headers=headers,
                timeout=5,
            )

            if response_dir.status_code == 200:
                direccion_id = response_dir.json().get("iddireccion")

                # Actualizar dirección
                payload_dir = {
                    "descripciondir": direccion,
                    "region_id": int(region_id),
                    "usuario_id": username,
                }
                print(payload_dir)

                response_update_dir = requests.put(
                    f"{settings.API_BUSINESS_URL}/direcciones/{direccion_id}",
                    headers=headers,
                    json=payload_dir,
                    timeout=5,
                )

                if response_user.status_code in [
                    200,
                    204,
                ] and response_update_dir.status_code in [200, 204]:
                    messages.success(
                        request, "¡Perfil y dirección modificados correctamente!"
                    )
                else:
                    messages.error(
                        request,
                        "No se pudo actualizar correctamente el perfil o la dirección.",
                    )
            else:
                messages.error(request, "No se pudo obtener la dirección del usuario.")

        except Exception as e:
            messages.error(request, f"Error al actualizar: {e}")

    try:
        response_user = requests.get(
            f"{settings.API_AUTH_URL}/usuarios/{username}", headers=headers, timeout=5
        )
        usuario = response_user.json() if response_user.status_code == 200 else {}

        response_dir = requests.get(
            f"{settings.API_BUSINESS_URL}/direcciones/usuario/{username}",
            headers=headers,
            timeout=5,
        )
        direccion = response_dir.json() if response_dir.status_code == 200 else {}

        regiones = requests.get(f"{settings.API_BUSINESS_URL}/regiones").json()
        comunas = requests.get(f"{settings.API_BUSINESS_URL}/comunas").json()

        contexto = {
            "usuario": usuario,
            "direccion": direccion,
            "region": regiones,
            "comuna": comunas,
        }

        return render(request, "Inicio/perfil_usuario.html", contexto)

    except Exception as e:
        messages.error(request, f"Error al cargar el perfil: {e}")
        return redirect("inicio")


# -------------------- PRODUCTOS --------------------
# MICROFONOS
def mostrarMic(request):
    username = request.session.get("username")
    token = request.session.get("token")

    if not username or not token:
        messages.error(request, "Debes iniciar sesión para ver los productos.")
        return redirect("iniciar")

    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(
            f"{settings.API_BUSINESS_URL}/productos/tipo/1", headers=headers, timeout=5
        )

        if response.status_code == 200:
            productos = response.json()
        else:
            productos = []
            messages.error(request, "No se pudieron obtener los productos.")

        contexto = {
            "mic": productos,
        }

        return render(request, "Inicio/microfonos.html", contexto)

    except Exception as e:
        messages.error(request, f"Error al cargar productos: {e}")
        return redirect("inicio")


def detalleProducto(request, id):

    try:
        response = requests.get(
            f"{settings.API_BUSINESS_URL}/productos/{id}", timeout=5
        )
        if response.status_code == 200:
            producto = response.json()
            contexto = {"producto": producto}
            return render(request, "Inicio/detalle_producto.html", contexto)
        else:
            messages.error(request, "Producto no encontrado.")
            return redirect("inicio")
    except Exception as e:
        messages.error(request, f"Error al obtener el producto: {e}")
        return redirect("inicio")


def micadmin(request, id):
    micros = Producto.objects.filter(tipoprod=1)
    usuario = Usuario.objects.get(username=id)
    contexto = {"mic": micros, "usuario": usuario}
    return render(request, "Inicio/micadmin.html", contexto)


def micro(request, idmic):
    producto = Producto.objects.get(idProducto=idmic)
    contexto = {"prod": producto}
    return render(request, "Inicio/mic1.html", contexto)


# TECLADOS
def mostrarTeclado(request, id):
    teclados = Producto.objects.filter(tipoprod=2)
    usuario = Usuario.objects.get(username=id)
    contexto = {"teclado": teclados, "usuario": usuario}
    return render(request, "Inicio/teclados.html", contexto)


def tecladoadmin(request, id):
    teclados = Producto.objects.filter(tipoprod=2)
    usuario = Usuario.objects.get(username=id)
    contexto = {"teclado": teclados, "usuario": usuario}
    return render(request, "Inicio/tecladoadmin.html", contexto)


def teclado(request, idk, usuario):
    productos = Producto.objects.get(idProducto=idk)
    username = Usuario.objects.get(username=usuario)
    contexto = {"prod": productos, "usuario": username}
    return render(request, "Inicio/mic1.html", contexto)


# MOUSES
def mostrarMouse(request, id):
    mouses = Producto.objects.filter(tipoprod=5)
    usuario = Usuario.objects.get(username=id)
    contexto = {"mouse": mouses, "usuario": usuario}
    return render(request, "Inicio/mouses.html", contexto)


def mouseAdmin(request, id):
    mouses = Producto.objects.filter(tipoprod=5)
    usuario = Usuario.objects.get(username=id)
    contexto = {"mouse": mouses, "usuario": usuario}
    return render(request, "Inicio/mouseAdmin.html", contexto)


def mouse(request, idm, usuario):
    usuario = Usuario.objects.get(username=usuario)
    productos = Producto.objects.get(idProducto=idm)
    contexto = {"prod": productos, "usuario": usuario}
    return render(request, "Inicio/mic1.html", contexto)


# GRAFICAS
def mostrarGrafica(request, id):
    graficas = Producto.objects.filter(tipoprod=3)
    usuario = Usuario.objects.get(username=id)
    contexto = {"grafica": graficas, "usuario": usuario}
    return render(request, "Inicio/graficas.html", contexto)


def graficaAdmin(request, id):
    graficas = Producto.objects.filter(tipoprod=3)
    usuario = Usuario.objects.get(username=id)
    contexto = {"grafica": graficas, "usuario": usuario}
    return render(request, "Inicio/graficaAdmin.html", contexto)


def grafica(request, idg, usuario):
    productos = Producto.objects.get(idProducto=idg)
    usuario = Usuario.objects.get(username=usuario)
    contexto = {"prod": productos, "usuario": usuario}
    return render(request, "Inicio/mic1.html", contexto)


# PROCESADORES
def mostrarProcesador(request, id):
    procesadores = Producto.objects.filter(tipoprod=6)
    usuario = Usuario.objects.get(username=id)
    contexto = {"procesador": procesadores, "usuario": usuario}
    return render(request, "Inicio/procesadores.html", contexto)


def procesadorAdmin(request, id):
    procesadores = Producto.objects.filter(tipoprod=6)
    usuario = Usuario.objects.get(username=id)
    contexto = {"procesador": procesadores, "usuario": usuario}
    return render(request, "Inicio/procesadorAdmin.html", contexto)


def procesador(request, idp, usuario):
    productos = Producto.objects.get(idProducto=idp)
    usuario = Usuario.objects.get(username=usuario)
    contexto = {"prod": productos, "usuario": usuario}
    return render(request, "Inicio/mic1.html", contexto)


# RAMS
def mostrarRam(request, id):
    rams = Producto.objects.filter(tipoprod=4)
    usuario = Usuario.objects.get(username=id)
    contexto = {"ram": rams, "usuario": usuario}
    return render(request, "Inicio/rams.html", contexto)


def ramAdmin(request, id):
    rams = Producto.objects.filter(tipoprod=4)
    usuario = Usuario.objects.get(username=id)
    contexto = {"ram": rams, "usuario": usuario}
    return render(request, "Inicio/ramAdmin.html", contexto)


def ram(request, idr, usuario):
    productos = Producto.objects.get(idProducto=idr)
    usuario = Usuario.objects.get(username=usuario)
    contexto = {"prod": productos, "usuario": usuario}
    return render(request, "Inicio/mic1.html", contexto)


def registrarse(request):
    try:
        response_regiones = requests.get(
            f"{settings.API_BUSINESS_URL}/regiones", timeout=5
        )
        response_comunas = requests.get(
            f"{settings.API_BUSINESS_URL}/comunas", timeout=5
        )

        regiones = (
            response_regiones.json() if response_regiones.status_code == 200 else []
        )
        comunas = response_comunas.json() if response_comunas.status_code == 200 else []

        contexto = {"regiones_m": regiones, "comunas_m": comunas}
    except Exception as e:
        messages.error(request, f"No se pudieron cargar los datos: {e}")
        contexto = {"regiones_m": [], "comunas_m": []}

    return render(request, "Inicio/registrarse.html", contexto)


def registrar_m(request):
    if request.method == "POST":
        user = request.POST["usuario"]
        contra = request.POST["contra"]
        correo = request.POST["email"]
        nombree = request.POST["nombre"]
        apellido = request.POST["apellido"]

        # Validación de contraseñas
        if request.POST["contra"] != request.POST["contra2"]:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect("registrarse")

        payload_usuario = {
            "username": user,
            "contrasennia": contra,
            "nombre": nombree,
            "apellido": apellido,
            "email": correo,
            "tipousuario_id": 2,  # usuario normal
        }

        try:
            # Crear el usuario en la API_AUTH
            response_usuario = requests.post(
                f"{settings.API_AUTH_URL}/usuarios", json=payload_usuario, timeout=5
            )

            print(f"Enviando a: {settings.API_AUTH_URL}/usuarios")
            print("Payload:", payload_usuario)

            if response_usuario.status_code in [200, 201]:
                # Si se creó correctamente el usuario, ahora registramos su dirección
                direccion = request.POST["direccion"]
                region = request.POST["region"]  # Este valor ya es el ID

                payload_direccion = {
                    "usuario_id": user,
                    "descripciondir": direccion,
                    "region_id": int(region),
                }

                print(f"Enviando a: {settings.API_BUSINESS_URL}/direcciones")
                print("Payload:", payload_direccion)

                response_direccion = requests.post(
                    f"{settings.API_BUSINESS_URL}/direcciones",
                    json=payload_direccion,
                    timeout=5,
                )

                if response_direccion.status_code in [200, 201]:
                    return redirect("iniciar")
                else:
                    messages.error(
                        request,
                        "Usuario creado, pero ocurrió un error al guardar la dirección.",
                    )
            else:
                messages.error(
                    request, "No se pudo registrar el usuario. Verifica los datos."
                )
        except Exception as e:
            messages.error(request, f"Error de conexión: {str(e)}")

    return redirect("registrarse")


def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST.get("usuario")
        password = request.POST.get("contra")

        try:
            response = requests.post(
                f"{settings.API_AUTH_URL}/usuarios/login",
                json={"username": username, "contrasennia": password},
                timeout=5,
            )
            if response.status_code == 200:
                data = response.json()
                usuario_api = data["usuario"]
                token = data["access_token"]

                request.session["token"] = token
                request.session["username"] = usuario_api["username"]
                request.session["tipousuarioId"] = usuario_api["tipousuarioId"]
                request.session["usuario_api"] = usuario_api
                request.session.modified = True

                if usuario_api["tipousuarioId"] == 1:
                    return redirect("menu_admin")
                return redirect("inicio")

            messages.error(request, "Credenciales inválidas")
        except requests.RequestException:
            messages.error(request, "No se pudo conectar con la API")

    return redirect("iniciar")


def newProd(request):
    nombre = request.POST["nomprod"]
    tipoProd = request.POST["tipoprod"]
    marca = request.POST["marcaprod"]
    stock = request.POST["stockprod"]
    imagen = request.FILES["imgprod"]
    desc = request.POST["descprod"]
    precio = request.POST["precio"]

    idProd2 = TipoProd.objects.get(idTiporod=tipoProd)
    marca2 = Marca.objects.get(idMarca=marca)
    existe = None
    try:
        existe = Producto.objects.get(nombreProducto=nombre)
        messages.error(request, "El producto ya existe")
        return redirect("addprod")
    except:
        Producto.objects.create(
            nombreProducto=nombre,
            precioProducto=precio,
            especificacionProd=desc,
            stockProd=stock,
            imagenProd=imagen,
            tipoprod=idProd2,
            marca=marca2,
        )
        return redirect("menu_admin")


def eliminarProducto(request, idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    producto.delete()

    messages.success(request, "¡Producto Eliminado!")

    return redirect("indexadmin")


def edicionProducto(request, idProducto):
    token = request.session.get("token")
    headers = {"Authorization": f"Bearer {token}"} if token else {}

    try:
        response_producto = requests.get(
            f"{settings.API_BUSINESS_URL}/productos/{idProducto}",
            headers=headers,
            timeout=5,
        )
        producto = (
            response_producto.json() if response_producto.status_code == 200 else None
        )

        response_tipos = requests.get(
            f"{settings.API_BUSINESS_URL}/tipoproducto", timeout=5
        )
        tipos = response_tipos.json() if response_tipos.status_code == 200 else []

        response_marcas = requests.get(f"{settings.API_BUSINESS_URL}/marcas", timeout=5)
        marcas = response_marcas.json() if response_marcas.status_code == 200 else []

        if not producto:
            messages.error(request, "Producto no encontrado")
            return redirect("indexadmin")

        return render(
            request,
            "Inicio/edicionProducto.html",
            {
                "producto": producto,
                "tipoProd": tipos,
                "Marca": marcas,
            },
        )

    except Exception as e:
        messages.error(request, f"Error al obtener datos del producto: {e}")
        return redirect("indexadmin")


def editarProducto(request, idProducto):
    if request.method == "POST":
        token = request.session.get("token")
        headers = {"Authorization": f"Bearer {token}"} if token else {}

        payload = {
            "nombreproducto": request.POST.get("nomprod"),
            "tipoprod_id": int(request.POST.get("tipoprod")),
            "marca_id": int(request.POST.get("marcaprod")),
            "stockprod": int(request.POST.get("stockprod")),
            "precioproducto": float(request.POST.get("precio")),
            "especificacionprod": request.POST.get("descprod"),
        }

        files = {}
        if request.FILES.get("imgprod"):
            files["imagenprod"] = request.FILES["imgprod"]

        try:
            response = requests.put(
                f"{settings.API_BUSINESS_URL}/productos/{idProducto}",
                headers=headers,
                json=payload,
                timeout=5,
            )
            if response.status_code in [200, 204]:
                messages.success(request, "¡Producto modificado correctamente!")
            else:
                messages.error(request, f"Error {response.status_code}: No se pudo modificar.")
        except Exception as e:
            messages.error(request, f"Error al conectar con la API: {e}")

    return redirect("indexadmin")


def agregar_producto(request, idProducto, usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=idProducto)
    contexto = {"producto": producto, "usuario": usuario2}
    carrito.agregar(producto)
    return render(request, "Inicio/carrito.html", contexto)


def eliminar_producto(request, idProducto, usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=idProducto)
    contexto = {"producto": producto, "usuario": usuario2}
    carrito.eliminar(producto)
    return render(request, "Inicio/carrito.html", contexto)


def restar_producto(request, idProducto, usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=idProducto)
    contexto = {"producto": producto, "usuario": usuario2}
    carrito.restar(producto)
    return render(request, "Inicio/carrito.html", contexto)


def limpiar_producto(request, usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    contexto = {"usuario": usuario2}
    carrito.limpiar()
    return render(request, "Inicio/carrito.html", contexto)


def recuperar_contrasena(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            response = requests.post(
                f"{settings.API_AUTH_URL}/usuarios/recover",
                json={"email": email},
                timeout=5,
            )
            if response.status_code == 200:
                data = response.json()
                return render(
                    request,
                    "Inicio/recovery_pass.html",
                    {"mensaje": data.get("message", "Contraseña restablecida.")},
                )
            else:
                return render(
                    request,
                    "Inicio/recovery_pass.html",
                    {
                        "error": "No se pudo recuperar la contraseña. Revisa el correo ingresado."
                    },
                )
        except Exception as e:
            return render(
                request,
                "Inicio/recovery_pass.html",
                {"error": f"Error de conexión: {str(e)}"},
            )

    return render(request, "Inicio/recovery_pass.html")
