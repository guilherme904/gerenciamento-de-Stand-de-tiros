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

    @classmethod
    def cadastrar_cliente(cls):
        clientes = cls._get_clientes_obj()

        print("\n--- Cadastro de Novo Cliente ---")
        id_novo = input("ID do Cliente (Curto Ex: C001): ").upper()
        nome = input("Nome do Cliente: ")
        cpf = input("CPF do Cliente: ")
        
        if cls._buscar_cliente(clientes, id_novo):
            print(f"❌ Erro: ID {id_novo} já está em uso.")
            cls._aguardar()
            return
            
        novo_cliente = Cliente(id_novo, nome, cpf)
        clientes.append(novo_cliente)
        cls._salvar_clientes(clientes)
        print(f"\n✅ Cliente '{nome}' cadastrado com sucesso! ID: \033[92m{novo_cliente.id}\033[0m")
        cls._aguardar()

    @classmethod
    def listar_clientes(cls):
        clientes = cls._get_clientes_obj()
        
        if not clientes:
            print("\n🚨 Nenhum cliente cadastrado.")
            cls._aguardar()
            return
            
        print("\n\033[34m### Clientes Cadastrados ###\033[0m")
        for cliente in clientes:
            print(f"ID: {cliente.id} | Nome: {cliente.nome} | CPF: {cliente.cpf}")
        print("----------------------------")
        cls._aguardar()

    @classmethod
    def cadastrar_equipamento(cls):
        equipamentos = cls._get_equipamentos_obj()

        print("\n--- Cadastro de Equipamento/Munição ---")
        id_novo = input("ID do Equipamento (Curto Ex: E01): ").upper()
        nome = input("Nome do Item: ")
        tipo = input("Tipo (Arma ou Munição): ").capitalize()
        
        if tipo not in ["Arma", "Munição"]:
            print("❌ Tipo inválido.")
            cls._aguardar()
            return
        
        try:
            quantidade = int(input("Quantidade inicial em estoque: "))
        except ValueError:
            print("❌ Quantidade inválida.")
            cls._aguardar()
            return
        
        if cls._buscar_equipamento(equipamentos, id_novo):
            print(f"❌ Erro: ID {id_novo} já está em uso.")
            cls._aguardar()
            return
            
        novo_equipamento = Equipamento(id_novo, nome, tipo, quantidade) 
        equipamentos.append(novo_equipamento)
        cls._salvar_equipamentos(equipamentos)
        print(f"\n✅ {nome} adicionado. ID: \033[92m{novo_equipamento.id}\033[0m")
        cls._aguardar()

    @classmethod
    def listar_estoque(cls):
        equipamentos = cls._get_equipamentos_obj()
        
        if not equipamentos:
            print("\n🚨 Estoque vazio.")
            cls._aguardar()
            return
            
        print("\n\033[34m### Estoque Atual ###\033[0m")
        for eq in equipamentos:
            print(f"ID: {eq.id} | {eq.nome} ({eq.tipo}): {eq.quantidade} em estoque")
        print("----------------------")
        cls._aguardar()