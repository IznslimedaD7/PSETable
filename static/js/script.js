let ml = document.getElementsByClassName('menu-list')
let tb = document.getElementsByClassName('table')
function animation(){
	for (let i = 0; i < tb.length; i++) { 
			tb[i].classList.add('anim'); 
}
}
window.onload = animation;

function docReady(fn) {
    if (document.readyState === "complete" || document.readyState === "interactive") {
        setTimeout(fn, 1);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}  
docReady(function(){
let mb = document.getElementById('menuBut')
console.log(mb)

mb.onclick = function (){
	for (let i = 0; i < ml.length; i++) { 
			ml[i].classList.add('vis'); 
}}});

docReady(function(){
	let bb = document.getElementById('backarrow')
	bb.onclick = function (){
	for (let i = 0; i < ml.length; i++) { 
			ml[i].classList.remove('vis'); 
}}})
