const esqueciSenha = document.querySelector('.esqueci-senha');
const passwordInput = document.querySelector('#password');
const togglePassword = document.querySelector('.toggle-password');

togglePassword.addEventListener('click', () => {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
    togglePassword.classList.toggle('fa-eye-slash');
});

const loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', function(e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = passwordInput.value;

    if (!email || !password) {
        alert('Preencha todos os campos!');
        return;
    }
    
    window.location.href = "admin.html";
});
