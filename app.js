function checkLogin() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username === 'admin' && password === 'admin') {
        window.location.href = 'admin.html'; // Redirecciona a la página del administrador.
        return false; // Evita la recarga de la página.
    } else {
        alert('Usuario o contraseña incorrectos.');
        return false; // Evita la recarga de la página.
    }
}
