function abrirModal(titulo, conteudoHTML) {
    document.getElementById("modalTitulo").innerHTML = titulo;
    document.getElementById("modalConteudo").innerHTML = conteudoHTML;

    document.getElementById("modalOverlay").style.display = "flex";
}

function fecharModal() {
    document.getElementById("modalOverlay").style.display = "none";
}

// ==========================
// ALUNOS
// ==========================
async function carregarAlunos() {
    const r = await fetch("/gestao/dados/alunos");
    const dados = await r.json();

    let html = "<ul>";
    dados.forEach(a => {
        html += `
        <li>
            <strong>${a.nome}</strong> — ${a.email} — Status: ${a.status_pagamento}
            
            <button class="btn-editar" onclick="editarAluno(${a.id})">Editar</button>
            <button class="btn-excluir" onclick="excluirAluno(${a.id})">Excluir</button>
        </li>`;
    });
    html += "</ul>";

    abrirModal("Lista de Alunos", html);
}

// ==========================
// PROFESSORES
// ==========================
async function carregarProfessores() {
    const r = await fetch("/gestao/dados/professores");
    const dados = await r.json();

    let html = "<ul>";
    dados.forEach(p => {
        html += `
        <li>
            <strong>${p.nome}</strong>

            <button class="btn-editar" onclick="editarProfessor(${p.id})">Editar</button>
            <button class="btn-excluir" onclick="excluirProfessor(${p.id})">Excluir</button>
        </li>`;
    });
    html += "</ul>";

    abrirModal("Lista de Professores", html);
}

// ==========================
// ESTÚDIOS
// ==========================
async function carregarEstudios() {
    const r = await fetch("/gestao/dados/estudios");
    const dados = await r.json();

    let html = "<ul>";
    dados.forEach(e => {
        html += `
        <li>
            <strong>${e.nome}</strong> — ${e.endereco}

            <button class="btn-editar" onclick="editarEstudio(${e.id})">Editar</button>
            <button class="btn-excluir" onclick="excluirEstudio(${e.id})">Excluir</button>
        </li>`;
    });
    html += "</ul>";

    abrirModal("Lista de Estúdios", html);
}

// ==========================
// PAGAMENTOS ATRASADOS
// ==========================
async function carregarPagamentosAtrasados() {
    const r = await fetch("/gestao/dados/pagamentos_atrasados");
    const dados = await r.json();

    let html = "<ul>";
    dados.forEach(a => {
        html += `
        <li>
            <strong>${a.nome}</strong> — ${a.email}

            <button class="btn-editar" onclick="editarAluno(${a.id})">Editar</button>
            <button class="btn-excluir" onclick="excluirAluno(${a.id})">Excluir</button>
        </li>`;
    });
    html += "</ul>";

    abrirModal("Pagamentos Atrasados", html);
}


async function excluirAluno(id) {
    if (!confirm("Tem certeza que deseja excluir este aluno?")) return;

    const r = await fetch(`/gestao/aluno/${id}`, { method: "DELETE" });
    const res = await r.json();

    alert(res.mensagem || res.erro);

    fecharModal();
}

async function excluirProfessor(id) {
    if (!confirm("Tem certeza que deseja excluir este professor?")) return;

    const r = await fetch(`/gestao/professor/${id}`, { method: "DELETE" });
    const res = await r.json();

    alert(res.mensagem || res.erro);

    fecharModal();
}

async function excluirEstudio(id) {
    if (!confirm("Tem certeza que deseja excluir este estúdio?")) return;

    const r = await fetch(`/gestao/estudio/${id}`, { method: "DELETE" });
    const res = await r.json();

    alert(res.mensagem || res.erro);

    fecharModal();
}

function abrirModalEdicaoAluno(aluno) {
    const html = `
        <label>Nome:</label>
        <input id="editNome" class="modal-input" value="${aluno.nome}">
        
        <label>Email:</label>
        <input id="editEmail" class="modal-input" value="${aluno.email}">
        
        <label>CPF:</label>
        <input id="editCpf" class="modal-input" value="${aluno.cpf}">
        
        <label>Status Pagamento:</label>
        <select id="editStatus" class="modal-input">
            <option value="pendente" ${aluno.status_pagamento === "pendente" ? "selected" : ""}>Pendente</option>
            <option value="pago" ${aluno.status_pagamento === "pago" ? "selected" : ""}>Pago</option>
            <option value="atrasado" ${aluno.status_pagamento === "atrasado" ? "selected" : ""}>Atrasado</option>
        </select>

        <button class="btnSalvar" onclick="salvarEdicaoAluno(${aluno.id})">Salvar</button>
    `;

    abrirModal("Editar Aluno", html);
}

async function salvarEdicaoAluno(id) {
    const nome = document.getElementById("editNome").value;
    const email = document.getElementById("editEmail").value;
    const cpf = document.getElementById("editCpf").value;
    const status_pagamento = document.getElementById("editStatus").value;

    const payload = {
        nome,
        email,
        cpf,
        status_pagamento
    };

    const r = await fetch(`/gestao/aluno/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    const res = await r.json();
    alert(res.mensagem || res.erro);

    fecharModal();
}

async function editarAluno(id) {
    const r = await fetch(`/gestao/dados/alunos`);
    const dados = await r.json();

    // Buscar aluno pelo ID
    const aluno = dados.find(a => a.id === id);

    if (!aluno) {
        alert("Aluno não encontrado!");
        return;
    }

    abrirModalEdicaoAluno(aluno);
}


function abrirModalEdicaoProfessor(professor) {
    const html = `

        <label>Nome:</label>
        <input id="editProfNome" class="modal-input" value="${professor.nome || ""}">

        <label>Email:</label>
        <input id="editProfEmail" class="modal-input" value="${professor.email || ""}">

        <label>CREF:</label>
        <input id="editProfCref" class="modal-input" value="${professor.cref || ""}">

        <label>Identificador:</label>
        <input id="editProfIdentificador" class="modal-input" value="${professor.identificador || ""}">

        <label>Tipo Identificador:</label>
        <select id="editProfTipoIdentificador" class="modal-input">
            <option value="cpf" ${professor.tipo_identificador === "cpf" ? "selected" : ""}>CPF</option>
            <option value="cref" ${professor.tipo_identificador === "cref" ? "selected" : ""}>CREF</option>
        </select>

        <label>Ativo:</label>
        <input id="editProfAtivo" type="checkbox" ${professor.ativo ? "checked" : ""}>

        <label>ID do Estúdio:</label>
        <input id="editProfEstudio" type="number" class="modal-input" value="${professor.estudio_id || ""}">

        <button class="btnSalvar" onclick="salvarEdicaoProfessor(${professor.id})">Salvar</button>
    `;

    abrirModal("Editar Professor", html);
}

async function salvarEdicaoProfessor(id) {
    const payload = {
        nome: document.getElementById("editProfNome").value,
        email: document.getElementById("editProfEmail").value,
        cref: document.getElementById("editProfCref").value,
        identificador: document.getElementById("editProfIdentificador").value,
        tipo_identificador: document.getElementById("editProfTipoIdentificador").value,
        ativo: document.getElementById("editProfAtivo").checked,
        estudio_id: Number(document.getElementById("editProfEstudio").value)
    };

    const r = await fetch(`/gestao/professor/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    const res = await r.json();
    alert(res.mensagem || res.erro);

    fecharModal();
}

async function editarProfessor(id) {
    const r = await fetch(`/gestao/dados/professores`);
    const dados = await r.json();

    const professor = dados.find(p => p.id === id);

    if (!professor) {
        alert("Professor não encontrado!");
        return;
    }

    abrirModalEdicaoProfessor(professor);
}
