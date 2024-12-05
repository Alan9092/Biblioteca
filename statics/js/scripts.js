document.getElementById('emailForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const errorMessage = document.getElementById('error-message');
    const spinner = document.getElementById('spinner-email');
    const nextStepButton = document.getElementById('nextStep');

    spinner.style.display = 'inline-block';
    nextStepButton.disabled = true;

    fetch('/login/validar-correo/', {
        method: 'POST',
        body: new URLSearchParams({'email': email}),
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    })
    .then(response => response.json())
    .then(data => {
        spinner.style.display = 'none';
        nextStepButton.disabled = false;

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
        spinner.style.display = 'none';
        nextStepButton.disabled = false;
    });
});

document.getElementById('fase2Form').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('displayEmail').textContent;
    const password = document.getElementById('password').value;
    const spinner = document.getElementById('spinner-password');
    const btnText = document.getElementById('btnText');
    const errorContainer = document.getElementById('error-container');

    spinner.style.display = 'inline-block';
    btnText.style.display = 'none';

    fetch('/login/validar-password/', {
        method: 'POST',
        body: new URLSearchParams({'email': email, 'password': password}),
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    })
    .then(response => response.json())
    .then(data => {
        spinner.style.display = 'none';
        btnText.style.display = 'inline';

        if (data.valid) {
            window.location.href = data.redirect_url;
        } else {
            errorContainer.style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        spinner.style.display = 'none';
        btnText.style.display = 'inline';
    });
});