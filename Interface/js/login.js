document.addEventListener('DOMContentLoaded', function(){
    // Validación de formulario


    eventListeners();
});

function eventListeners(){
    passwordValidation();
}

function passwordValidation(){
    const button = document.querySelector('.btn');
    button.addEventListener('click', (e)=>{
        e.preventDefault();
        console.log('Oprimiendo boton');
    })

}