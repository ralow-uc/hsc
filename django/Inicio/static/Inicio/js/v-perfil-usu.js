var nomusu = document.getElementById("nomusu");
var apeusu = document.getElementById("apepusu");
var usuario = document.getElementById("username");
var numusu = document.getElementById("numusu");
var reg = document.getElementById("regionusu");
var mailusu = document.getElementById("mailusu");
var mensajes = document.getElementById("mensajes1");
var mensajes2 = document.getElementById("mensajes2");
const formulario = document.getElementById("form1");


formulario.addEventListener("submit", e =>{
  e.preventDefault();
  let mensajesMostrar = "";
  let entrar = false;
  let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
  let usuario = /^[a-zA-Z0-9\_\-]{4,16}$/
  mensajes.innerHTML = "";
  mensajes2.innerHTML = "";

  if(nomusu.value==""){
    mensajesMostrar += 'El nombre del producto no puede estar vacío. <br>';
    entrar= true;

  }
  if(apeusu.value==""){
    mensajesMostrar += 'El nombre del producto no puede estar vacío. <br>';
    entrar= true;

  }
  if (!usuario.test(username.value)) {
    mensajesMostrar += 'El nombre de usuario no es válido. <br>';
    entrar = true;
  }
  if(dirusu.value==""){
    mensajesMostrar += 'La dirección no puede estar vacío. <br>';
    entrar= true;

  }
  if (reg.value === "Selecciona una región"){
    mensajesMostrar += 'Seleccione una región. <br>'
    entrar = true
  }
  if (!regexEmail.test(mailusu.value)) {
    mensajesMostrar += 'El correo electrónico ingresado no es válido. <br>'
    entrar = true
  }


  if (entrar) {
    mensajes.innerHTML = mensajesMostrar;
  } 
  else {
      mensajes2.innerHTML = "Enviado";
  }
})


