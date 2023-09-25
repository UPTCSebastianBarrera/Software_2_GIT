document.getElementById("experienciaForm").addEventListener("submit", function (event) {
    event.preventDefault();

    // Obtener los valores del formulario
    const valoracion = parseInt(document.getElementById("valoracion").value);
    const comentario = document.getElementById("comentario").value;

    // Validar la valoración (debe estar entre 0 y 5)
    if (valoracion < 0 || valoracion > 5) {
        alert("La valoración debe estar entre 0 y 5 estrellas.");
        return;
    }

    // Obtener las experiencias almacenadas en Local Storage (si existen)
    let experiencias = localStorage.getItem("experiencias");
    experiencias = experiencias ? JSON.parse(experiencias) : [];

    // Crear un nuevo objeto de experiencia
    const nuevaExperiencia = {
        valoracion: valoracion,
        comentario: comentario,
        fecha: new Date().toLocaleString(), // Puedes personalizar el formato de fecha
    };

    // Agregar la nueva experiencia a la lista
    experiencias.push(nuevaExperiencia);

    // Guardar las experiencias actualizadas en Local Storage
    localStorage.setItem("experiencias", JSON.stringify(experiencias));

    alert("Experiencia guardada exitosamente.");
    // Puedes redirigir al usuario a otra página o hacer cualquier otra acción aquí.

    // Limpiar el formulario
    document.getElementById("valoracion").value = "";
    document.getElementById("comentario").value = "";
});
