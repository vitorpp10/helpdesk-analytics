import os
import random
from datetime import datetime, timedelta

import psycopg

with ( 
    psycopg.connect(
        host="localhost", 
        port=55432, 
        dbname="chamados_db",  
        user="chamados_user", 
        password=os.environ["POSTGRES_PASSWORD"],
    ) as conn,
    conn.cursor() as cur,
):
    print("Conexão com o banco OK")

CATEGORIAS = ["hardware", "rede", "software", "acesso", "impressora"]
PRIORIDADES = ["baixa", "media", "alta", "critica"]
STATUS = ["aberto", "em_andamento", "resolvido"]
SETORES = ["Financeiro", "RH", "TI", "Marketing"]

for _ in range(5):
    dias_atras = random.randint(0, 90)
    criado_em = datetime.now() - timedelta(days=dias_atras)
    status = random.choice(STATUS)
    setor = random.choice(SETORES)
    categoria = random.choices(
        CATEGORIAS,
        weights=[15, 20, 30, 25, 10],
        k=1
    )[0]
    prioridade = random.choices(
        PRIORIDADES,
        weights=[30, 25, 15, 5],
        k=1
    )[0]
    if status == "resolvido":
        minutos_para_resolver = random.randint(5, 480)
    else:
        minutos_para_resolver = None
    print(
        f"Setor: {setor} | Cat: {categoria} | Prio: {prioridade} | "
        f"Status: {status} | Criado: {criado_em:%Y-%m-%d %H:%M} | "
        f"Tempo: {minutos_para_resolver if minutos_para_resolver is not None else 'N/A'}"
    )