O projeto simula uma API interna de chamados de TI, mas usando apenas dados falsos. A ideia é ter um sistema pequeno o suficiente para você entender inteiro. mas completo o bastante para treinar exatamente o tipo de coisa que pode aparecer em produtos ou contextos reais: Python + SQL + Lógica + Manipulação de dados.

```txt 
chamados-api/
├── app/
│   └── main.py
├── scripts/
│   └── seed.py
├── sql/
│   └── schema.sql
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── .env.example
```

`app/main.py` → entrada da FastAPI e nossas rotas.
`scripts/seed.py` → script separado para gerar os 500 chamados falsos.
`sql/schema.sql` → definição da estrutura do banco. Aqui ficará o CREATE TABLE.
`docker-compose.yml` → descreve como subir o PostgreSQL sem instalar/configurar tudo manualmente.
`requirements.txt` → dependências Python do projeto.
`.gitignore` → impede arquivos locais/sensíveis de irem para o Git, principalmente .env.
`.env.example` → mostra quais variáveis são necessárias, mas sem senha real.

O `seed.py` fica separado porque gerar dados é uma responsabilidade diferente de executar a API, e não queremos que os dados sejam recriados toda vez que a aplicação iniciar.

---

**Colocar no `requirements.txt` e depois instalar**:

```bash
pip install nome_modulo
pip freeze > requirements.txt
python3 -m pip install -r requirements.txt
``` 

**Rodar aplicação**:

```bash
python scripts/seed.py
``` 