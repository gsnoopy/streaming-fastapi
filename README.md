# Streaming FastAPI

### Build da imagem Docker

```bash
docker-compose build
```

### Subir o container (modo interativo)

```bash
docker-compose up
```

### Subir o container (modo background/detached)

```bash
docker-compose up -d
```

### Parar os containers

```bash
docker-compose down
```

---

## Rodar os testes com pytest

Rodar todos os testes:

```bash
pytest tests/
```

Rodar um arquivo específico:

```bash
pytest tests/categories.py
```

Rodar com mais detalhes (verbose):

```bash
pytest -v tests/categories.py
```

---

## Comandos Alembic (migrações)

Criar uma nova migration com autogenerate:

```bash
alembic revision --autogenerate -m "mensagem da migration"
```

Aplicar todas as migrations pendentes (upgrades):

```bash
alembic upgrade head
```

Reverter uma migration (downgrade) para uma versão específica:

```bash
alembic downgrade <revision_id>
```

---

## Configurações e variáveis de ambiente

```env
DATABASE_URL=postgresql://usuario:senha@host:porta/banco
TEST_DATABASE_URL=postgresql://usuario:senha@host:porta/banco
SECRET_KEY=sua_chave_secreta
```