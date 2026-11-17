CREATE TABLE IF NOT EXISTS chamados (
    id SERIAL PRIMARY KEY,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    setor TEXT,
    categoria TEXT,
    prioridade TEXT,
    status TEXT,
    minutos_para_resolver INTEGER
);
