var nombre = document.getElementById("Username");
var contra1 = document.getElementById("contra");
var reg = document.getElementById("region");


const form = document.getElementById("form1");
var mensaje = document.getElementById("warnings");

form.addEventListener("submit", e =>{
    let mensajesMostrar = "";
    let entrar = false;
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
    let usuario1 = /^[a-zA-Z0-9\_\-]{4,16}$/
    mensaje.innerHTML = "";
    if (!usuario1.test(usuario.value)) {
        mensajesMostrar += 'El nombre de usuario no es válido. <br>';
        entrar = true;
    }



    if (!regexEmail.test(email.value)) {
        mensajesMostrar += 'El correo electrónico ingresado no es válido. <br>'
        entrar = true
    }
    if (reg.value === "Selecciona una región"){
      mensajesMostrar += 'Seleccione una región. <br>'
      entrar = true
    }
    if (comuna.value === "Selecciona una Comuna"){
        mensajesMostrar += 'Seleccione una Comuna. <br>'
        entrar = true
      }

    if (contra1.value.length < 4 || contra1.value.length > 16) {
        mensajesMostrar += 'La contraseña no tiene el largo necesario. <br>';
        entrar = true;
    }
    if (contra1.value != contra2.value) {
        mensajesMostrar += 'Las contraseña no coinciden <br>';
        entrar = true;

    }
    if (entrar) {
        mensaje.innerHTML = mensajesMostrar;
        e.preventDefault();
    } else {
        mensaje.innerHTML = "Enviado";
    }
})
