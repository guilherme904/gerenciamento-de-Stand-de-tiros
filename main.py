import os
from stand_tiros import GerenciadorStand, CLIENTES_FILE, ESTOQUE_FILE, _salvar_dados

def menu():
    if not os.path.exists(CLIENTES_FILE):
        _salvar_dados(CLIENTES_FILE, [])
    if not os.path.exists(ESTOQUE_FILE):
        _salvar_dados(ESTOQUE_FILE, [])
        
    while True:
        os.system("cls" if os.name == 'nt' else "clear") 

        print("""
        __________________________________________________________
                    🎯\033[92mSISTEMA DE GERENCIAMENTO DE STAND DE TIROS\033[0m🎯
        ___________________________MENU__________________________
                   
        \033[94m-- Escolha uma das opções --\033[0m
              
        1️⃣  - Cadastrar Cliente
              
        2️⃣  - Listar Clientes
              
        3️⃣  - Cadastrar Novo Equipamento/Munição (Entrada Inicial)
              
        4️⃣ - Listar Estoque (Armas e Munições)

        0️⃣  - \033[91mSair\033[0m
        __________________________________________________________
        """)

        OP = input("Escolha uma opção: ")

        if OP == "1":
            GerenciadorStand.cadastrar_cliente()

        elif OP == "2":
            GerenciadorStand.listar_clientes()

        elif OP == "3":
            GerenciadorStand.cadastrar_equipamento()

        elif OP == "5":
            GerenciadorStand.listar_estoque()
            
        elif OP == "0":
            print("Saindo do Sistema...")
            break
        else:
            print("❌ Opção inválida, tente novamente.")
            GerenciadorStand._aguardar()


if __name__ == "__main__":
    menu()