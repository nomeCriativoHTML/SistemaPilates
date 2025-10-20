# Sistema Pilates

README atualizado com a estrutura completa do projeto, instruções para rodar e pontos importantes.

## Visão geral
Sistema web leve usando FastAPI + Jinja2 para gerenciar alunos, professores, estúdios, agendas, agendamentos e evoluções.

## Estrutura completa do projeto
- README.md
- .env
- requirements.txt
- alembic.ini
- Dockerfile
- main.py
- alembic/
  - env.py
  - script.py.mako
  - versions/
    - aaab08ca480d_initial_tables.py
- app/
  - __init__.py
  - core/
    - __init__.py
    - config.py
  - database/
    - __init__.py
    - connection.py
  - models/
    - __init__.py
    - aluno.py
    - professor.py
    - estudio.py
    - admin.py
    - enums.py
    - relacionamentos/
      - __init__.py
      - agenda.py
      - agendamentos.py
  - schema/
    - __init__.py
    - aluno.py
    - professor.py
    - estudio.py
    - admin.py
    - agenda.py
    - agendamento.py
    - evolucao.py
  - controllers/
    - __init__.py
    - aluno_controller.py
    - professor_controller.py
    - estudio_controller.py
    - admin_controller.py
    - agenda_controller.py
    - agendamento_controller.py
    - evolucao_controller.py
  - routes/
    - __init__.py
    - aluno_routes.py
    - professor_routes.py
    - estudio_routes.py
    - admin_routes.py
    - login_routes.py
    - agenda_routes.py
    - agendamento_routes.py
    - evolucao_routes.py
  - templates/
    - base.html
    - cadastro.html
    - login.html
    - aluno.html
    - professor.html
    - estudio.html
    - admin.html
    - agenda.html
    - agendamento.html
    - evolucao.html
  - static/
    - JS/
      - cadastro.js
      - login.js
      - agenda.js
      - agendamento.js
      - evolucao.js
    - CSS/
      - cadastro.css
      - login.css
      - aluno.css
      - professor.css
      - estudio.css
      - admin.css
      - agenda.css
      - agendamento.css
      - evolucao.css
    - images/
  - utils/
    - __init__.py
    - auth.py
    - helpers.py
  - tests/
    - __init__.py
    - test_models.py
    - test_controllers.py
    - test_routes.py
    - test_integration.py

## Fluxo e responsabilidades
1. Rotas (app/routes/) recebem requisições e injetam dependências (get_db).
2. Controllers (app/controllers/) implementam regras de negócio e chamam models.
3. Models (app/models/) representam a camada de persistência (SQLAlchemy).
4. Schemas (app/schema/) validam e serializam dados (Pydantic).
5. Templates + static servem a interface web (Jinja2).

## Como rodar localmente (passo a passo)
1. Criar e ativar virtualenv:
```sh
python -m venv .venv
.\.venv\Scripts\activate
```
2. Instalar dependências:
```sh
pip install -r requirements.txt
```
3. Configurar variáveis em `.env` (ex.: DATABASE_URL, SECRET_KEY).
4. Rodar migrações Alembic:
```sh
alembic upgrade head
```
5. Iniciar aplicação:
```sh
uvicorn main:app --reload
```

Com Docker:
- Build: docker build -t sistemapilates .
- Run: docker run --env-file .env -p 8000:8000 sistemapilates

## Endpoints principais (exemplos)
- HTML:
  - GET /login
  - GET /alunos/cadastro
  - GET /agenda
- API:
  - POST /api/alunos/ — cria aluno
  - GET /api/alunos/{id} — obtém aluno
  - POST /api/agendamentos/ — cria agendamento

(Ver arquivos em app/routes/ para lista completa de rotas.)

## Notas importantes
- Conexão com DB: app/database/connection.py — exporta engine, Base, SessionLocal e get_db.
- Migrações: alembic/ está configurado para importar modelos (ver alembic/env.py).
- Autenticação: utilitário em app/utils/auth.py (tokens/sessões).
- Testes: app/tests/ contém unit/integration; execute com pytest.
- Organização: separar lógica em controllers; rotas apenas expõem e validam entrada via schemas.

## Como contribuir
- Siga a estrutura: routes → controllers → models → schema → templates/static.
- Adicione testes para novas features.
- Antes do PR: rode pytest e alembic upgrade head.

---
