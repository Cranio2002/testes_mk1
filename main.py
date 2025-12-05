#!/usr/bin/env python3
from alunos import GrupoCapoeira

def menu():
    grupo = GrupoCapoeira()

    while True:
        print('\n==== SISTEMA DE GERENCIAMENTO DO GRUPO DE CAPOEIRA LIBERDADE ====')
        print("\n=== Menu ===")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Gerar carteirinha por ID")
        print("4. Editar aluno")
        print("5. Remover aluno")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                aluno = grupo.cadastro()
                grupo.saudacao(aluno)
                grupo.carteirinha(aluno)
            case '2':
                grupo.mostrar_alunos()
            case '3':
                id_busca = input("Digite o ID do aluno: ")
                aluno = grupo.procurar_aluno(id_busca)
                if aluno:
                    grupo.carteirinha(aluno)
                else:
                    print("❌ Aluno não encontrado.")
            case '4':
                id_busca = input("Digite o ID do aluno para editar: ")
                grupo.editar_aluno(id_busca)
            case '5':
                id_busca = input("Digite o ID do aluno para remover: ")
                grupo.remover_aluno(id_busca)
            case '0':
                print("Saindo do sistema. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
