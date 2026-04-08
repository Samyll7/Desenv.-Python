from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import Union

app = FastAPI(
    title="Calculadora API",
    description="Uma API simples para realizar operações matemáticas básicas.",
    version="1.0.0"
)

class Operacao(str, Enum):
    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"

class CalculoRequest(BaseModel):
    numero1: float
    numero2: float
    operacao: Operacao

class CalculoResponse(BaseModel):
    resultado: float
    operacao: str
    mensagem: str

@app.post("/calcular", response_model=CalculoResponse)
async def calcular(request: CalculoRequest):
    num1 = request.numero1
    num2 = request.numero2
    op = request.operacao
    
    resultado = 0.0
    
    if op == Operacao.soma:
        resultado = num1 + num2
    elif op == Operacao.subtracao:
        resultado = num1 - num2
    elif op == Operacao.multiplicacao:
        resultado = num1 * num2
    elif op == Operacao.divisao:
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Divisão por zero não é permitida.")
        resultado = num1 / num2
    
    return {
        "resultado": resultado,
        "operacao": op.value,
        "mensagem": f"Operação de {op.value} realizada com sucesso."
    }

@app.get("/")
async def root():
    return {"mensagem": "Bem-vindo à API de Calculadora. Acesse /docs para a documentação Swagger."}
