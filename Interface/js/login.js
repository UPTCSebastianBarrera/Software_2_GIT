document.getElementById("ingresarBtn").addEventListener("click", function() {
    const usuarioInput = document.getElementById("usuarioInput").value;
    const contrasenaInput = document.getElementById("contrasenaInput").value;

    fetch("/Software_2_GIT/Interface/assets/users.json") // Cargamos el archivo JSON
        .then(response => response.json())
        .then(data => {
            const usuarios = data.usuarios;
            const usuarioValido = usuarios.find(user => user.mail === usuarioInput && user.password === contrasenaInput);
            if (usuarioValido) {
                alert("Inicio de sesión exitoso.");
                // Aquí puedes redirigir al usuario a otra página si es necesario.
            } else {
                alert("Credenciales incorrectas. Por favor, inténtalo de nuevo.");
            }
        })
        .catch(error => {
            console.error("Error al cargar el archivo JSON: " + error);
        });
});