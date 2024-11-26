document.getElementById('emailForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const errorMessage = document.getElementById('error-message');
    const nextStepButton = document.getElementById('nextStep');
    const spinner = document.getElementById('spinner');  // Obtenemos el spinner

    // Mostrar el spinner y ocultar el botón "Siguiente"
    spinner.style.display = 'inline-block';
    nextStepButton.style.display = 'none';

    fetch('/login/validar-correo/', {
        method: 'POST',
        body: new URLSearchParams({
            'email': email
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Ocultar el spinner y mostrar el botón "Siguiente"
        spinner.style.display = 'none';
        nextStepButton.style.display = 'inline';

        if (data.valid) {
            document.getElementById('fase1').style.display = 'none';
            document.getElementById('fase2').style.display = 'block';
            document.getElementById('displayEmail').textContent = email;
        } else {
            errorMessage.style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        // Ocultar el spinner y mostrar el botón "Siguiente" en caso de error
        spinner.style.display = 'none';
        nextStepButton.style.display = 'inline';
    });
});

document.getElementById('fase2').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('displayEmail').textContent;
    const password = document.getElementById('password').value;
    const signInButton = document.getElementById('signIn');
    const spinner = document.getElementById('spinner');  // Obtenemos el spinner
    const btnText = document.getElementById('btnText');  // Obtenemos el texto del botón

    // Mostrar el spinner y ocultar el texto del botón "Iniciar sesión"
    spinner.style.display = 'inline-block';
    btnText.style.display = 'none';

    fetch('/login/validar-password/', {
        method: 'POST',
        body: new URLSearchParams({
            'email': email,
            'password': password
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Ocultar el spinner y mostrar el texto del botón "Iniciar sesión"
        spinner.style.display = 'none';
        btnText.style.display = 'inline';

        if (data.valid) {
            // Redirige al index si la contraseña es correcta
            window.location.href = data.redirect_url;
        } else {
            // Limpiar mensajes de error previos
            const existingError = document.getElementById('error-container');
            if (existingError) {
                existingError.remove(); // Elimina el mensaje de error anterior
            }

            // Crear un nuevo contenedor de error
            const errorContainer = document.createElement('div');
            errorContainer.id = 'error-container'; // Asignar un ID único
            errorContainer.style.color = 'red';
            errorContainer.style.textAlign = 'center';
            errorContainer.style.marginTop = '10px';
            errorContainer.innerHTML = `<p>Contraseña incorrecta</p>`;
            
            // Agregar el mensaje de error al formulario de la fase 2
            document.getElementById('fase2').appendChild(errorContainer);
        }
    })
    .catch(error => {
        // Ocultar el spinner y mostrar el texto del botón "Iniciar sesión" en caso de error
        spinner.style.display = 'none';
        btnText.style.display = 'inline';
        console.error('Error:', error);
    });
});
