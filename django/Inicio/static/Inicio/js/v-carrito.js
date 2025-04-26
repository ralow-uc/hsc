var item1 = document.getElementById("item1");
var item2 = document.getElementById("item2");
var item3 = document.getElementById("item3");
var iteminv = document.getElementById("iteminvisible");
var iteminv2 = document.getElementById("iteminvisible2");
var iteminv3 = document.getElementById("iteminvisible3");
iteminv.style.display='none';
iteminv2.style.display='none';
iteminv3.style.display='none';

function eliminar(){
    item1.style.display='none';
    iteminv.style.display='';
}
function eliminar2(){
    item2.style.display='none';
    iteminv2.style.display='';
}
function eliminar3(){
    item3.style.display='none';
    iteminv3.style.display='';
}