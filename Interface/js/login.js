document.getElementById("ingresarBtn").addEventListener("click", function() {
    const usuarioInput = document.getElementById("usuarioInput").value;
    const contrasenaInput = document.getElementById("contrasenaInput").value;

    // Expresión regular para validar el formato del correo electrónico
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

    // Expresión regular para validar la contraseña (mínimo 6 caracteres)
    const passwordRegex = /^.{3,}$/;

    if (!emailRegex.test(usuarioInput)) {
        alert("Por favor, ingresa un correo electrónico válido.");
        return;
    }

    if (!passwordRegex.test(contrasenaInput)) {
        alert("La contraseña debe tener al menos 6 caracteres.");
        return;
    }

    fetch("/Software_2_GIT/Interface/assets/users.json") // Cargamos el archivo JSON
        .then(response => response.json())
        .then(data => {
            const usuarios = data.usuarios;
            const usuarioValido = usuarios.find(user => user.mail === usuarioInput && user.password === contrasenaInput);
            if (usuarioValido) {
                alert("Inicio de sesión exitoso.");
                window.location.href = "page1.html";
            } else {
                alert("Credenciales incorrectas. Por favor, inténtalo de nuevo.");
            }
        })
        .catch(error => {
            console.error("Error al cargar el archivo JSON: " + error);
        });
});
