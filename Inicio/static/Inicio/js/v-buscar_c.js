var idprod = document.getElementById("idprod");
var mensaje1= document.getElementById("mensajes1");

const tabla1 = document.getElementById("tabla1");
const tabla2 = document.getElementById("tabla2");

tabla1.style.display= 'none';
tabla2.style.display= 'none';

function mostrar(){
  if(idprod.value == ""){
    mensaje1.style.display='block';
    tabla1.style.display= 'none';
    tabla2.style.display= 'none';
    mensaje1.innerHTML= "El ID del producto no puede estar vacío.";
  }
  if (idprod.value == "01"){
    tabla2.style.display= 'none';
    mensaje1.style.display='none';
    tabla1.style.display= 'table';

  }
  if (idprod.value == "02"){
    tabla1.style.display= 'none';
    mensaje1.style.display='none';
    tabla2.style.display= 'table';

  }
}