var clave = document.getElementById("Email1");


const form = document.getElementById("form1");
var mensaje = document.getElementById("warnings");

form.addEventListener("submit", e =>{
    e.preventDefault();
    let mensajesMostrar = "";
    let entrar = false;
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
    mensaje.innerHTML = "";

    if (!regexEmail.test(Email1.value)) {
        mensajesMostrar += 'El correo electrónico ingresado no es válido. <br>'
        entrar = true
    }
    if (entrar) {
        mensaje.innerHTML = mensajesMostrar;
    } else {
        mensaje.innerHTML = "Se ha enviado un correo para recuperar su contraseña";
    }
})