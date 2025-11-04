const esqueciSenha = document.querySelector('.esqueci-senha');
const passwordInput = document.querySelector('#password');
const togglePassword = document.querySelector('.toggle-password');

togglePassword.addEventListener('click', () => {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
    togglePassword.classList.toggle('fa-eye-slash');
});

const loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = passwordInput.value;

    if (!email || !password) {
        alert('Preencha todos os campos!');
        return;
    }

    try {
        // Envia os dados para o endpoint de login
        const response = await fetch("/login/aluno", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"  // necessário para form HTML
            },
            body: new URLSearchParams({
                email: email,
                password: password
            })
        });

        const result = await response.json();

        if (response.ok) {
            // Login bem-sucedido
            console.log("Token JWT:", result.token); // opcional, salvar em localStorage/sessionStorage
            alert(result.mensagem);
            // Redireciona para página de aluno
            window.location.href = "/login/aluno";  // corresponde à rota acima
        } else {
            // Erro no login
            alert(result.error);
        }
    } catch (error) {
        console.error("Erro ao fazer login:", error);
        alert("Erro inesperado. Tente novamente.");
    }
});
