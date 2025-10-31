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

class GerenciadorStand:
    
    @staticmethod
    def _aguardar():
        input("\nPressione ENTER para continuar...")

    @staticmethod
    def _get_clientes_obj():
        dados = _carregar_dados(CLIENTES_FILE)
        clientes_ajustados = []
        for d in dados:
            clientes_ajustados.append(Cliente(d['id'], d['nome'], d['cpf']))
        return clientes_ajustados

    @staticmethod
    def _get_equipamentos_obj():
        dados = _carregar_dados(ESTOQUE_FILE)
        return [Equipamento(**d) for d in dados]

    @staticmethod
    def _salvar_clientes(clientes_obj):
        clientes_dict = [c.to_dict() for c in clientes_obj]
        _salvar_dados(CLIENTES_FILE, clientes_dict)

    @staticmethod
    def _salvar_equipamentos(equipamentos_obj):
        equipamentos_dict = [e.to_dict() for e in equipamentos_obj]
        _salvar_dados(ESTOQUE_FILE, equipamentos_dict)

    @classmethod
    def _buscar_cliente(cls, clientes, id_procurado):
        for cliente in clientes:
            if cliente.id == id_procurado.upper():
                return cliente
        return None
        
    @classmethod
    def _buscar_equipamento(cls, equipamentos, id_procurado):
        for eq in equipamentos:
            if eq.id == id_procurado.upper():
                return eq
        return None
