from fastapi import FastAPI, HTTPException
import os
import psycopg2

app = FastAPI()



clientesId = [1,2,3,4,5]

@app.get("/")
def hello_world():

    try:
        conn = psycopg2.connect(user="admin",
                                  password="123",
                                  host="db",
                                  port="5432",
                                  database="rinha")
        cursor = conn.cursor()
    except:
        print("I am unable to connect to the database")

    

    return {"message": os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")}

@app.post("/clientes/{id}/transacoes")
def executa_transacao(id: int):
    if id in clientesId:
        return {"limite": 100000, "saldo" : -9098}
    else:
        raise HTTPException(status_code=404)

@app.get("/clientes/{id}/extrato")
def extrato(id: int):
    if id in clientesId:
        return {
                "saldo": {
                    "total": -9098,
                    "data_extrato": "2024-01-17T02:34:41.217753Z",
                    "limite": 100000
                },
                "ultimas_transacoes": [
                    {
                    "valor": 10,
                    "tipo": "c",
                    "descricao": "descricao",
                    "realizada_em": "2024-01-17T02:34:38.543030Z"
                    },
                    {
                    "valor": 90000,
                    "tipo": "d",
                    "descricao": "descricao",
                    "realizada_em": "2024-01-17T02:34:38.543030Z"
                    }
                ]
            }
    else:
        raise HTTPException(status_code=404)