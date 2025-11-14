function abrirModal(titulo, conteudoHTML) {
    document.getElementById("modalTitulo").innerHTML = titulo;
    document.getElementById("modalConteudo").innerHTML = conteudoHTML;

    document.getElementById("modalOverlay").style.display = "flex";
}

function fecharModal() {
    document.getElementById("modalOverlay").style.display = "none";
}


async function carregarAlunos() {
    const r = await fetch("/gestao/dados/alunos");
    const dados = await r.json();

    let html = "<ul>";
    dados.forEach(a => {
        html += `<li><strong>${a.nome}</strong> — ${a.email} — Status: ${a.status_pagamento}</li>`;
    });
    html += "</ul>";

    abrirModal("Lista de Alunos", html);
}

async function carregarProfessores() {
    const r = await fetch("/gestao/dados/professores");
    const dados = await r.json();

    let html = "<ul>";
    dados.forEach(p => {
        html += `<li><strong>${p.nome}</strong></li>`;
    });
    html += "</ul>";

    abrirModal("Lista de Professores", html);
}

async function carregarEstudios() {
    const r = await fetch("/gestao/dados/estudios");
    const dados = await r.json();

    let html = "<ul>";
    dados.forEach(e => {
        html += `<li><strong>${e.nome}</strong> — ${e.endereco}</li>`;
    });
    html += "</ul>";

    abrirModal("Lista de Estúdios", html);
}

async function carregarPagamentosAtrasados() {
    const r = await fetch("/gestao/dados/pagamentos_atrasados");
    const dados = await r.json();

    let html = "<ul>";
    dados.forEach(a => {
        html += `<li><strong>${a.nome}</strong> — ${a.email}</li>`;
    });
    html += "</ul>";

    abrirModal("Pagamentos Atrasados", html);
}