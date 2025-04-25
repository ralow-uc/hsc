//OBTENER VARIABLES
var idprod = document.getElementById("idprod");
var nomprod = document.getElementById("nombreprod");
var mensaje1= document.getElementById("mensajes1");
var mensaje2= document.getElementById("mensajes2");
var tipoprod= document.getElementById("tipoprod");
var marcaprod= document.getElementById("marcaprod");
var stockprod= document.getElementById("stockprod");
const formulario = document.getElementById("form2");
var descprod = document.getElementById("txtarea");
//Para visualizar y poner datos del formulario
formulario.style.display= 'none';
function mostrar(){
  if(idprod.value == ""){
    mensaje1.style.display='block';
    formulario.style.display= 'none';
    mensaje1.innerHTML= "El ID del producto no puede estar vacío.";
  }
  if (idprod.value == "01"){
    mensaje1.style.display='none';
    formulario.style.display= 'block';
    //Nombre producto
    nomprod.value = "Quadcast";
    //Función para sacar el valor del select
    tipoprod.addEventListener("change", function(){
      console.log(tipoprod.value)
    });
    //Marca del producto
    marcaprod.value="HyperX";
    //Stock del producto
    stockprod.value="10"
    //Tipo de producto
    tipoprod.value = "microfono";
    //Descripción del producto
    descprod.innerHTML = "El HyperX QuadCast™ es el micrófono independiente todo incluido ideal para el aspirante a streamer o podcaster que busca un micrófono de condensador con sonido de calidad. QuadCast viene con su propio soporte antivibraciones para ayudar a reducir los ruidos de la vida diaria y un filtro pop incorporado para amortiguar los molestos sonidos explosivos. Podrás conocer al instante el estado del micrófono gracias al indicador LED y silenciar con un sencillo toque para evitar problemas de retransmisión inesperados. Con cuatro patrones polares seleccionables, este micrófono está preparado para casi cualquier situación de grabación y también cuenta con un dial de control de ganancia convenientemente ubicado para ajustar rápidamente la sensibilidad de entrada de tu micrófono. El adaptador de montaje incluido se ajusta a roscas de 3/8 ”y 5/8” y es compatible con la mayoría de los soportes. El modelo QuadCast S proporciona iluminación RGB y efectos dinámicos que se pueden personalizar a través del software HyperX NGENUITY.";

  }
  //Validar el segundo formulario
  formulario.addEventListener("submit", e =>{
    e.preventDefault();
    let mensajemostrar= "";
    let entrar= false;
    mensaje2.innerHTML= "";
    var mensaje3= document.getElementById("mensajes3");
    mensaje3.innerHTML= "";



    if(nomprod.value== ""){
      mensajemostrar+= "El producto debe llevar un nombre. <br>";
      entrar=true;
    }
    if(descprod.value== ""){
      mensajemostrar+= "El producto debe llevar una descripción. <br>";
      entrar=true;
    }
    if(marcaprod.value== ""){
      mensajemostrar+= "El producto debe tener una marca.";
      entrar=true;
    }
    if(stockprod.value== ""){
      mensajemostrar+= "El producto debe tener stock.";
      entrar=true;
    }
    if(entrar){
      mensaje2.innerHTML= mensajemostrar;
    }
    else{
      mensaje3.innerHTML="Producto modificado correctamente!"
    }

  })

};