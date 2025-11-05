const passwordInput = document.querySelector('#password');
const togglePassword = document.querySelector('.toggle-password');
const loginForm = document.getElementById('loginForm');
const userButtons = document.querySelectorAll(".user-btn");

let tipoLogin = null;

// Selecionar tipo de usuário
userButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        userButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");

        if (btn.id === "btnAluno") tipoLogin = "aluno";
        if (btn.id === "btnProfessor") tipoLogin = "professor";
        if (btn.id === "btnAdmin") tipoLogin = "admin";

        loginForm.setAttribute("action", `/login/${tipoLogin}`);
    });
});

// Mostrar/ocultar senha
togglePassword.addEventListener('click', () => {
    const type = passwordInput.type === 'password' ? 'text' : 'password';
    passwordInput.type = type;
    togglePassword.classList.toggle('fa-eye-slash');
});

// Enviar login
loginForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    if (!tipoLogin) {
        alert("Escolha o tipo de usuário.");
        return;
    }

    const email = document.getElementById('email').value;
    const password = passwordInput.value;

    if (!email || !password) {
        alert('Preencha todos os campos!');
        return;
    }

    let endpoint = `/login/${tipoLogin}`;

    try {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams({ email, password })
        });

        const result = await response.json();

        if (!response.ok) {
            alert(result.error || "Credenciais inválidas");
            return;
        }

        alert(result.message || "Login realizado!");

        // Rotas corretas para redirecionamento
        if (tipoLogin === "aluno") {
            window.location.href = "/login/aluno";
        } else if (tipoLogin === "professor") {
            window.location.href = "/login/professor/dashboard";
        } else if (tipoLogin === "admin") {
            window.location.href = "/admin/dashboard";
        }

    } catch (error) {
        console.error("Erro ao fazer login:", error);
        alert("Erro inesperado. Tente novamente.");
    }
});
