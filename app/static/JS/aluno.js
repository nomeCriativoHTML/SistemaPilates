
const navItems = document.querySelectorAll(".bottom-nav .nav-item");


navItems.forEach(item => {
    const label = item.querySelector("span").textContent.trim();

    switch(label) {
        case "Início":
            item.addEventListener("click", () => {
                window.location.href = "/alunos/aluno"; 
            });
            break;
        case "Agenda":
            item.addEventListener("click", () => {
                window.location.href = "/alunos/agenda"; 
            });
            break;
        case "Evolução":
            item.addEventListener("click", () => {
                window.location.href = "/alunos/evolucao";
            });
            break;
        case "Perfil":
            item.addEventListener("click", () => {
                window.location.href = "/alunos/perfil"; 
            });
            break;
    }
});

