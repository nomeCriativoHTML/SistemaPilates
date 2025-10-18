// --- Abas ---
document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('ativo'));
        document.querySelectorAll('.formulario').forEach(f => f.classList.remove('ativo'));
        tab.classList.add('ativo');
        document.getElementById(`form-${tab.dataset.tab}`).classList.add('ativo');
    });
});

// --- Botão voltar ---
document.querySelector('.btn-voltar').addEventListener('click', () => window.history.back());

// --- Botão cancelar ---
document.querySelectorAll('.cancelar').forEach(btn => {
    btn.addEventListener('click', () => {
        if (confirm('Deseja cancelar o cadastro? Os dados não salvos serão perdidos.')) {
            window.location.href = '/home';
        }
    });
});

// --- Submit do formulário de aluno ---
document.getElementById('form-aluno').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    // Certifique-se que todos os campos da model estão presentes
    // incluindo cpf e senha
    const payload = {
        nome: data.nome,
        cpf: data.cpf,
        email: data.email,
        senha: data.senha,
        telefone: data.telefone || null,
        data_nascimento: data.data_nascimento || null,
        status_pagamento: data.status_pagamento || 'pendente'
    };

    try {
        const response = await fetch('/alunos/cadastro/aluno', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            alert('Aluno cadastrado com sucesso!');
            this.reset();
        } else {
            const error = await response.json();
            alert('Erro: ' + (error.error || 'Tente novamente.'));
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao cadastrar aluno. Verifique sua conexão.');
    }
});

// --- Máscara telefone ---
function mascaraTelefone(input) {
    const texto = input.value.replace(/\D/g, '');
    input.value = texto.replace(/^(\d{2})(\d{5})(\d{4})$/, '($1) $2-$3');
}
document.querySelectorAll('input[type="tel"]').forEach(input =>
    input.addEventListener('input', e => mascaraTelefone(e.target))
);
