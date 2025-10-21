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

// --- Submit do formulário de professor ---
document.getElementById('form-professor').addEventListener('submit', async function(e) {
    e.preventDefault();

    // Usar FormData diretamente para evitar erros de nome
    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    console.log('Dados brutos do formulário:', data);

    // Converter estudio_id para número ou null
    const estudioId = data.estudio_id ? parseInt(data.estudio_id) : null;
    
    // Converter ativo para boolean (checkbox retorna 'on' quando marcado)
    const ativo = data.ativo === 'on';

    const payload = {
        nome: data.nome,           
        cref: data.cref,
        email: data.email,
        senha: data.senha,
        telefone: data.telefone || null,
        identificador: data.identificador || null,
        tipo_identificador: data.tipo_identificador || null,
        estudio_id: estudioId,    
        ativo: ativo              
    };

    console.log('Payload final:', payload);

    // Validações
    if (!payload.nome) {
        alert('Nome é obrigatório!');
        return;
    }
    if (!payload.cref) {
        alert('CREF é obrigatório!');
        return;
    }
    if (!payload.email) {
        alert('Email é obrigatório!');
        return;
    }
    if (!payload.senha) {
        alert('Senha é obrigatória!');
        return;
    }

    try {
        const response = await fetch('/professores/cadastro/professor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        if (response.ok) {
            alert('Professor cadastrado com sucesso!');
            this.reset();
            // Reset do checkbox para checked
            document.getElementById('ativo').checked = true;
        } else {
            alert('Erro: ' + (result.error || 'Tente novamente.'));
        }
    } catch (error) {
        console.error('Erro completo:', error);
        alert('Erro ao cadastrar professor. Verifique sua conexão.');
    }
});

// --- Submit do formulário de estúdio ---
document.getElementById('form-estudio').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // TODO: Implementar lógica para cadastro de estúdio
    alert('Funcionalidade de cadastro de estúdio em desenvolvimento!');
});
// --- Máscaras CPF e Telefone (melhoradas e com limite) ---

// Função de máscara de telefone com limitação
function mascaraTelefone(input) {
    let valor = input.value.replace(/\D/g, '').slice(0, 11); // permite até 11 dígitos
    if (valor.length <= 10) {
        // formato fixo (10 dígitos)
        input.value = valor.replace(/^(\d{0,2})(\d{0,4})(\d{0,4})$/, function(_, ddd, p1, p2) {
            return `${ddd ? '(' + ddd : ''}${p1 ? ') ' + p1 : ''}${p2 ? '-' + p2 : ''}`;
        });
    } else {
        // formato celular (11 dígitos)
        input.value = valor.replace(/^(\d{0,2})(\d{0,5})(\d{0,4})$/, function(_, ddd, p1, p2) {
            return `${ddd ? '(' + ddd : ''}${p1 ? ') ' + p1 : ''}${p2 ? '-' + p2 : ''}`;
        });
    }
}

// Função de máscara de CPF com limitação
function mascaraCPF(input) {
    let valor = input.value.replace(/\D/g, '').slice(0, 11); // permite até 11 dígitos
    valor = valor.replace(/(\d{3})(\d)/, '$1.$2');
    valor = valor.replace(/(\d{3})(\d)/, '$1.$2');
    valor = valor.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
    input.value = valor;
}

// Aplicar a máscara de telefone a todos os inputs de telefone
document.querySelectorAll('input[type="tel"]').forEach(input => {
    input.addEventListener('input', e => mascaraTelefone(e.target));
});

// Aplicar máscara de CPF ao campo do aluno
const cpfInput = document.getElementById('cpf');
if (cpfInput) {
    cpfInput.addEventListener('input', e => mascaraCPF(e.target));
}

// Aplicar máscara de CPF ao identificador do professor quando o tipo for CPF
const identificadorInput = document.getElementById('identificador');
const tipoIdentificador = document.getElementById('tipo_identificador');
if (identificadorInput && tipoIdentificador) {
    identificadorInput.addEventListener('input', e => {
        if (tipoIdentificador.value === 'cpf') {
            mascaraCPF(e.target);
        } else {
            // Se for RG ou outro, só números, sem formatação
            e.target.value = e.target.value.replace(/\D/g, '').slice(0, 15);
        }
    });

    tipoIdentificador.addEventListener('change', () => {
        identificadorInput.value = ''; // limpa quando troca o tipo
    });
}

// --- Carregar estúdios para o select (opcional) ---
async function carregarEstudios() {
    try {
        // TODO: Implementar endpoint para listar estúdios
        // const response = await fetch('/estudios');
        // const estudios = await response.json();
        
        // Exemplo estático - substituir pela chamada real
        const estudios = [
            { id: 1, nome: 'Estúdio Central' },
            { id: 2, nome: 'Estúdio Zona Sul' }
        ];
        
        const select = document.getElementById('estudio_id');
        if (select) {
            estudios.forEach(estudio => {
                const option = document.createElement('option');
                option.value = estudio.id;
                option.textContent = estudio.nome;
                select.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Erro ao carregar estúdios:', error);
    }
}

// Carregar estúdios quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    carregarEstudios();
});

