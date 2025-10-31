import json
import os

CLIENTES_FILE = "clientes.json"
ESTOQUE_FILE = "estoque.json"

def _carregar_dados(filename):
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"⚠️ Aviso: Arquivo {filename} está corrompido ou vazio. Iniciando lista vazia.")
        return []

def _salvar_dados(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"❌ Erro ao salvar dados em {filename}: {e}")

class Cliente:
    
    def __init__(self, id, nome, cpf): 
        self.id = id
        self.nome = nome
        self.cpf = cpf

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
        }

class Equipamento:
    def __init__(self, id, nome, tipo, quantidade): 
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo,
            "quantidade": self.quantidade,
        }
