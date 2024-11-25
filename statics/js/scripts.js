// Base de datos simulada: lista de usuarios válidos
const users = [
    { email: "a20210155@utem.edu.mx", password: "123" },
    { email: "usuario2@example.com", password: "usuario2" },
    { email: "usuario3@example.com", password: "usuario3" },
];

// Referencias a elementos
const fase1 = document.getElementById("fase1");
const fase2 = document.getElementById("fase2");
const emailForm = document.getElementById("emailForm");
const emailInput = document.getElementById("email");
const displayEmail = document.getElementById("displayEmail");
const errorMessage = document.getElementById("error-message");
const passwordInput = document.getElementById("password");
const loginForm = document.querySelector("#fase2 form");

// Variables de estado
let currentUser = null;

// Manejo del formulario de correo electrónico (Fase 1)
emailForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Evitar recarga
    const email = emailInput.value;

    // Validar correo electrónico
    currentUser = users.find(user => user.email === email);
    if (currentUser) {
        // Mostrar segunda fase con animación
        displayEmail.textContent = email;
        fase1.style.display = "none";
        fase2.style.display = "block";
    } else {
        // Mostrar mensaje de error
        errorMessage.textContent = "Correo no válido.";
        errorMessage.style.display = "block";
    }
});

loginForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Evitar recarga
    const password = passwordInput.value;

    // Validar contraseña
    if (currentUser && currentUser.password === password) {
        // Redirigir a index.html
        window.location.href = "http://127.0.0.1:8000/"; // Cambia esta ruta si necesitas ajustar la ubicación
    } else {
        alert("Contraseña incorrecta.");
    }
});
