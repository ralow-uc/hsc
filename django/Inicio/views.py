from django.shortcuts import render,redirect
from .models import Usuario,Direccion,Comuna,Region,TipoUsuario, Producto, Marca,Categoria,TipoProd,Marca
from django.contrib import messages
from .Carrito import Carrito

# Create your views here.
def inicio(request):

    return render(request,'Inicio/index.html')
def inicioadmin(request):

    return render(request,'Inicio/index_admin.html') 
def vistamod(request):
    
    return render(request,'Inicio/modificar_producto.html')


def addprod (request):
    tipoProd = TipoProd.objects.all()
    marca = Marca.objects.all()
    contexto = {"tipoProd":tipoProd,"Marca":marca}

    return render (request,'Inicio/agregar_producto.html',contexto)   

def iniciar(request):

    return render(request,'Inicio/inicio_sesion.html')

def menuadmin(request):

    return render(request,'Inicio/dashboard-admin.html')

def carrito(request,id):
    usuario = Usuario.objects.get(username=id)
    contexto = {"usuario":usuario}
    return render(request,'Inicio/carrito.html', contexto)

def perfilusuario(request,id):
    usuario = Usuario.objects.get(username=id)
    contexto = {"usuario":usuario}
    
    return render(request,'Inicio/perfil-user.html',contexto)



def mostrarperfil(request,id):
    usuario = Usuario.objects.get(username=id)
    direccion = Direccion.objects.get(usuario=id)
    region = Region.objects.all()
    comuna = Comuna.objects.all()
    contexto = {"usuario":usuario, "direccion" : direccion,"region" : region,"comuna" : comuna}
    return render(request, 'Inicio/perfil_usuario.html',contexto)    

def modificarPerfil(request,id):
    usuario = Usuario.objects.get(username=id)
    contexto = {"usuario":usuario}
    usuario.username= request.POST.get('username')
    usuario.nombre = request.POST.get('nomusu')
    usuario.apellido = request.POST.get('apepusu')
    usuario.email = request.POST.get('mailusu')
    usuario.save()
    messages.success(request, '¡Perfil modificado correctamente!')
    return render (request,'Inicio/perfil-user.html',contexto)







# -------------------- PRODUCTOS --------------------
# MICROFONOS
def mostrarMic(request,id):
    micros = Producto.objects.filter(tipoprod=1)
    usuario = Usuario.objects.get(username=id)
    contexto = {"mic": micros,"usuario":usuario}
    return render(request, "Inicio/microfonos.html",contexto)

def micadmin (request,id):
    micros = Producto.objects.filter(tipoprod=1)
    usuario = Usuario.objects.get(username=id)
    contexto = {"mic": micros,"usuario":usuario}
    return render (request,'Inicio/micadmin.html',contexto) 
  
def micro(request,idmic,usuario):
    productos = Producto.objects.get(idProducto = idmic)
    username = Usuario.objects.get(username=usuario)
    contexto ={"prod": productos,"usuario":username} 
    return render(request, "Inicio/mic1.html",contexto)    



# TECLADOS
def mostrarTeclado(request, id):
    teclados = Producto.objects.filter(tipoprod=2)
    usuario = Usuario.objects.get(username=id)
    contexto= {"teclado": teclados,"usuario":usuario}
    return render(request, "Inicio/teclados.html",contexto)

def tecladoadmin (request,id):
    teclados = Producto.objects.filter(tipoprod=2)
    usuario = Usuario.objects.get(username=id)
    contexto = {"teclado": teclados,"usuario":usuario}
    return render (request,'Inicio/tecladoadmin.html',contexto) 

def teclado(request,idk, usuario):
    productos = Producto.objects.get(idProducto = idk)
    username = Usuario.objects.get(username=usuario)
    contexto = {"prod": productos,"usuario":username}
    return render(request, "Inicio/mic1.html",contexto)

# MOUSES
def mostrarMouse(request,id):
    mouses = Producto.objects.filter(tipoprod=5)
    usuario = Usuario.objects.get(username=id)
    contexto = {"mouse": mouses,"usuario":usuario}
    return render(request, "Inicio/mouses.html",contexto)

def mouseAdmin (request,id):
    mouses= Producto.objects.filter(tipoprod=5)
    usuario = Usuario.objects.get(username=id)
    contexto = {"mouse": mouses,"usuario":usuario}
    return render (request,'Inicio/mouseAdmin.html',contexto) 
    
def mouse(request,idm,usuario):
    usuario = Usuario.objects.get(username=usuario)
    productos = Producto.objects.get(idProducto = idm)
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto)    

# GRAFICAS
def mostrarGrafica(request,id):
    graficas = Producto.objects.filter(tipoprod=3)
    usuario = Usuario.objects.get(username= id)
    contexto = {"grafica": graficas,"usuario":usuario}
    return render(request, "Inicio/graficas.html",contexto)

def graficaAdmin (request,id):
    graficas= Producto.objects.filter(tipoprod=3)
    usuario = Usuario.objects.get(username=id)
    contexto ={"grafica": graficas,"usuario":usuario}
    return render (request,'Inicio/graficaAdmin.html',contexto) 
    
def grafica(request,idg,usuario):
    productos = Producto.objects.get(idProducto = idg)
    usuario = Usuario.objects.get(username= usuario)
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto)    

# PROCESADORES
def mostrarProcesador(request,id):
    procesadores = Producto.objects.filter(tipoprod=6)
    usuario = Usuario.objects.get(username= id)
    contexto = {"procesador": procesadores,"usuario":usuario}
    return render(request, "Inicio/procesadores.html",contexto)

def procesadorAdmin (request,id):
    procesadores= Producto.objects.filter(tipoprod=6)
    usuario = Usuario.objects.get(username= id)
    contexto = {"procesador": procesadores,"usuario":usuario}
    return render (request,'Inicio/procesadorAdmin.html',contexto) 
    
def procesador(request,idp,usuario):
    productos = Producto.objects.get(idProducto = idp)
    usuario = Usuario.objects.get(username= usuario)
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto)  

# RAMS
def mostrarRam(request,id):
    rams = Producto.objects.filter(tipoprod=4)
    usuario = Usuario.objects.get(username= id)
    contexto = {"ram": rams,"usuario":usuario}
    return render(request, "Inicio/rams.html",contexto)

def ramAdmin (request,id):
    rams= Producto.objects.filter(tipoprod=4)
    usuario = Usuario.objects.get(username= id)
    contexto = {"ram": rams,"usuario":usuario}
    return render (request,'Inicio/ramAdmin.html',contexto) 
    
def ram(request,idr,usuario):
    productos = Producto.objects.get(idProducto = idr)
    usuario = Usuario.objects.get(username= usuario)
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto )    











def registrarse(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    contexto = {"comunas_m": comunas,"regiones_m": regiones}
    return render(request,"Inicio/registrarse.html",contexto)

def registrar_m (request):
    user = request.POST['usuario']
    contra = request.POST['contra']
    correo = request.POST['email']
    region = request.POST['region']
    direccion = request.POST['direccion']
    comuna = request.POST['comuna']
    nombree = request.POST['nombre']
    apellido = request.POST['apellido']
    
    comuna2 = Comuna.objects.get(idComuna = comuna)
    region2 = Region.objects.get(idRegion = region)
    tipousuario2 = TipoUsuario.objects.get(idTipoUsuario = 2)
    existe = None
    try:
        existe = Usuario.objects.get(username=user)
        messages.error(request,'El usuario ya existe')
        return redirect ('registrarse')
    except:
        Usuario.objects.create(username = user , contrasennia = contra, nombre = nombree, apellido = apellido, email = correo,tipousuario = tipousuario2)
        x = Usuario.objects.get(username = user)
        Direccion.objects.create(descripcionDir = direccion, usuario = x,region = region2)
        return redirect ('iniciar')

        
def iniciar_sesion(request):
    usuario1 = request.POST['usuario']
    contra1 = request.POST['contra']
    try:
        usuario2 = Usuario.objects.get(username = usuario1,contrasennia = contra1)
        
        if(usuario2.tipousuario.idTipoUsuario == 1):
            return redirect ('menu_admin')
        else:    
            contexto = {"usuario":usuario2}
            
            return render(request, 'Inicio/index.html', contexto)            

    except:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        return redirect ('iniciar')
    
 






    
def newProd(request):
    nombre = request.POST['nomprod']
    tipoProd = request.POST['tipoprod']
    marca = request.POST['marcaprod']
    stock = request.POST['stockprod']
    imagen = request.FILES['imgprod']
    desc = request.POST['descprod']
    precio = request.POST['precio']
    
    idProd2 = TipoProd.objects.get(idTiporod = tipoProd)
    marca2 = Marca.objects.get(idMarca = marca)
    existe = None
    try:
        existe = Producto.objects.get(nombreProducto = nombre)
        messages.error(request,'El producto ya existe')
        return redirect ('addprod')
    except:
        Producto.objects.create(nombreProducto = nombre,precioProducto = precio,especificacionProd = desc,stockProd =stock,imagenProd = imagen,tipoprod = idProd2,marca = marca2)
        return redirect ('menu_admin')
    

def eliminarProducto(request, idProducto):
    producto= Producto.objects.get(idProducto=idProducto)
    producto.delete()

    messages.success(request, '¡Producto Eliminado!')

    return redirect('indexadmin')


 
def edicionProducto(request, idProducto):
    tipoProd = TipoProd.objects.all()
    marca = Marca.objects.all()
    producto = Producto.objects.get(idProducto=idProducto)

    return render(request,'Inicio/edicionProducto.html', {"producto": producto, "tipoProd":tipoProd,"Marca":marca})

def editarProducto(request,idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    tiprod1 =request.POST['tipoprod'] 
    tipoprod2 = TipoProd.objects.get(idTiporod =tiprod1)
    marca1 = request.POST['marcaprod']
    marca2 = Marca.objects.get(idMarca = marca1)
    if (request.FILES.get("imgprod")):
        fotoprod =  request.FILES['imgprod']
        producto.imagenProd = fotoprod
    producto.nombreProducto = request.POST.get('nomprod')
    producto.tipoprod = tipoprod2
    producto.marca = marca2
    producto.stockProd = request.POST.get('stockprod')
    producto.precioProducto = request.POST.get('precio')
    producto.especificacionProd = request.POST.get('descprod')
    producto.save()
    messages.success(request, '¡Producto Modificado!')
    return redirect('indexadmin')
    




def agregar_producto(request, idProducto, usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = idProducto)
    contexto = {"producto":producto,"usuario":usuario2}
    carrito.agregar(producto)
    return render(request,'Inicio/carrito.html',contexto)

def eliminar_producto(request, idProducto,usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = idProducto)
    contexto = {"producto":producto,"usuario":usuario2}
    carrito.eliminar(producto)
    return render(request,'Inicio/carrito.html',contexto)

def restar_producto(request, idProducto,usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = idProducto)
    contexto = {"producto":producto,"usuario":usuario2}
    carrito.restar(producto)
    return render(request,'Inicio/carrito.html',contexto)

def limpiar_producto(request,usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    contexto = {"usuario":usuario2}
    carrito.limpiar()
    return render(request,'Inicio/carrito.html',contexto)




