# FotoSocial API

API REST desenvolvida em Python com Flask, simulando o backend de uma rede social de fotos. Projeto final da disciplina de Cloud Computing — UNIDAVI 2026.

**Aluno:** Vinicius Policarpo Macedo  
**Tema:** 14 - Infraestrutura para uma Rede Social de Fotos

## Estrutura
trabalho-final-fotosocial/

├── api/
│   ├── app.py
│   ├── data/
│   │   └── fotos.json
│   └── tests/
│       └── test_api.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── requirements.txt
└── README.md

## Rotas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /status | Status da API |
| GET | /fotos | Lista todas as fotos |
| GET | /fotos/{id} | Retorna uma foto pelo ID |

## Como executar sem Docker

**Pré-requisitos:** Python 3.11+

```bash
pip install -r requirements.txt
cd api
python app.py
```

Acesse em `http://localhost:5000`

## Como executar com Docker

```bash
docker build -t fotosocial-api .
docker run -p 5000:5000 fotosocial-api
```

Acesse em `http://localhost:5000`

## Testes

```bash
python -m pytest api/tests/ -v
```