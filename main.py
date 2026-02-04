from db import conectar
from crud import inserir_usuarios, atualizar_usuario, deletar_usuario, consultar_banco


opcao = input(
    "Digite [1] Consultar | [2] Adicionar | [3] Editar | [4] Deletar: "
).strip()

# CONSULTAR BANCO DE DADOS
if opcao == "1":
    consultar_banco()
 
# INSERT USUÁRIO
elif opcao == "2":
    nome = input("Digite nome a ser adicionado: ")
    email = input("Digite email a ser adicionado: ")
    idade = int(input("Digite idade: "))
    inserir_usuarios(nome,email,idade)

#UPDATE USUÁRIO
elif opcao == "3":
    id_alt = int (input("Digite o ID: "))
    nome_alt = input("Digite nome a ser adicionado: ")
    email_alt = input("Digite email a ser adicionado: ")
    idade_alt = input("Digite idade: ")
    atualizar_usuario(nome_alt, email_alt, idade_alt, id_alt)

#DELETE USUÁRIO
elif opcao == "4":
    id_del = int(input("Id da conta para ser deletado: "))
    deletar_usuario(id_del)

else:
    print("Opção inválida!")

