# Sistema Pilates

README com visão geral, estrutura de pastas e instruções rápidas para rodar o projeto.

## Visão geral
Projeto backend/front-end leve usando FastAPI + Jinja2 para gerenciar alunos, professores, estúdios, agendas e evoluções.

## Estrutura principal (resumida)
- [main.py](main.py) — Ponto de entrada e configuração do FastAPI; variável de templates: [`templates`](main.py)
- [.env](.env) — Variáveis de ambiente (conexão MySQL)
- [requirements.txt](requirements.txt) — Dependências do projeto
- [alembic/](alembic/) — Migrations (ver [alembic/env.py](alembic/env.py) e [alembic/versions/aaab08ca480d_initial_tables.py](alembic/versions/aaab08ca480d_initial_tables.py))

Código da aplicação em `app/`:
- [app/database/connection.py](app/database/connection.py) — Engine SQLAlchemy, `Base`, `SessionLocal` e dependency [`get_db`](app/database/connection.py)
- [app/models/](app/models/) — Models SQLAlchemy (ver [app/models/__init__.py](app/models/__init__.py))
  - Principais models: [app/models/aluno.py](app/models/aluno.py), [app/models/professor.py](app/models/professor.py), [app/models/estudio.py](app/models/estudio.py), [app/models/admin.py](app/models/admin.py)
  - Enums: [app/models/enums.py](app/models/enums.py)
  - Relacionamentos: [app/models/relacionamentos/agenda.py](app/models/relacionamentos/agenda.py), [app/models/relacionamentos/agendamentos.py](app/models/relacionamentos/agendamentos.py)
- [app/schema/](app/schema/) — Schemas Pydantic (ex.: [app/schema/aluno.py](app/schema/aluno.py), [app/schema/professor.py](app/schema/professor.py), [app/schema/estudio.py](app/schema/estudio.py), [app/schema/admin.py](app/schema/admin.py))
  - Ex.: schema de entrada: [`AlunoCreate`](app/schema/aluno.py)
- [app/controllers/](app/controllers/) — Lógica de domínio / CRUD
  - Controle de alunos: [`AlunoController`](app/controllers/aluno_controller.py) e método [`AlunoController.criar_aluno`](app/controllers/aluno_controller.py)
  - Admin/gestão: [app/controllers/admin_controller.py](app/controllers/admin_controller.py)
- [app/routes/](app/routes/) — Routers FastAPI (ex.: [app/routes/aluno_routes.py](app/routes/aluno_routes.py), [app/routes/login_routes.py](app/routes/login_routes.py), [app/routes/admin_routes.py](app/routes/admin_routes.py))
  - Ex.: rota de cadastro de alunos: [`aluno_routes.pagina_cadastro`](app/routes/aluno_routes.py)
- [app/templates/](app/templates/) — Templates Jinja2 (ex.: [cadastro.html](app/templates/cadastro.html), [login.html](app/templates/login.html), [aluno.html](app/templates/aluno.html), [admin.html](app/templates/admin.html), [agenda.html](app/templates/agenda.html), [evolucao.html](app/templates/evolucao.html), [professor.html](app/templates/professor.html))
- [app/static/](app/static/) — Arquivos estáticos (JS/CSS)
  - JS: [app/static/JS/cadastro.js](app/static/JS/cadastro.js), [app/static/JS/login.js](app/static/JS/login.js), [app/static/JS/agenda.js](app/static/JS/agenda.js)
  - CSS: [app/static/CSS/cadastro.css](app/static/CSS/cadastro.css), [app/static/CSS/login.css](app/static/CSS/login.css), [app/static/CSS/aluno.css](app/static/CSS/aluno.css), [app/static/CSS/admin.css](app/static/CSS/admin.css), [app/static/CSS/agenda.css](app/static/CSS/agenda.css), [app/static/CSS/evolucao.css](app/static/CSS/evolucao.css), [app/static/CSS/professor.css](app/static/CSS/professor.css)

## Como rodar localmente
1. Criar e ativar virtualenv (ex. venv)
2. Instalar dependências:
```sh
pip install -r requirements.txt
```
3. Configurar `.env` (já existe em [`.env`](.env))
4. Rodar migrações Alembic (opcional / quando houver DB configurado):
```sh
alembic upgrade head
```
(arquivo de migrations: [alembic/versions/aaab08ca480d_initial_tables.py](alembic/versions/aaab08ca480d_initial_tables.py))

5. Iniciar servidor:
```sh
uvicorn main:app --reload
```

Rotas HTML principais:
- Página de cadastro: GET /alunos/cadastro (implementada em [app/routes/aluno_routes.py](app/routes/aluno_routes.py))
- Login: GET /login (ver [app/routes/login_routes.py](app/routes/login_routes.py))

API (exemplos):
- POST /alunos/ — cria um aluno via API (controller: [`AlunoController`](app/controllers/aluno_controller.py))
- POST /alunos/cadastro/aluno — endpoint usado pelo formulário (ver [app/routes/aluno_routes.py](app/routes/aluno_routes.py))

## Notas e pontos importantes
- Conexão com DB configurada em [app/database/connection.py](app/database/connection.py). Use [`get_db`](app/database/connection.py) como dependency nas rotas.
- Controllers encapsulam regra de negócio e persistência (ex.: [`AlunoController.criar_aluno`](app/controllers/aluno_controller.py)).
- Schemas Pydantic estão em [app/schema/](app/schema/) e servem para validação/serialização.
- Alembic está configurado para autogenerate (veja [alembic/env.py](alembic/env.py) que importa `app.models.*`).

## Contribuição
- Siga a estrutura: rotas em `app/routes/`, lógica em `app/controllers/`, models em `app/models/`, schemas em `app/schema/`, templates em `app/templates/` e estáticos em `app/static/`.
- Antes de abrir PR, rode migrações e testes (quando existirem).

--- 
