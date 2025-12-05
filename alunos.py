import json
from utils import gerar_id, ano_atual

DATA_FILE = "data.json"

class GrupoCapoeira:
    def __init__(self):
        self.data_base = self.carregar_alunos()

    # ----------------- CARREGAR E SALVAR -----------------
    def salvar_alunos(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data_base, f, ensure_ascii=False, indent=4)

    def carregar_alunos(self):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    # ----------------- CADASTRO -----------------
    def cadastro(self):
        nome = input("Digite seu nome e sobrenome: ")
        apelido = input("Digite seu apelido: ")
        idade = int(input("Digite sua idade: "))
        inscrito_ano = int(input("Digite o ano em que você se inscreveu no curso: "))

        aluno = {
            "id": gerar_id(),
            "nome": nome,
            "apelido": apelido,
            "idade": idade,
            "inscrito_ano": inscrito_ano
        }

        self.data_base.append(aluno)
        self.salvar_alunos()
        print(f"\n✅ Aluno cadastrado! ID: {aluno['id']}")
        return aluno

    # ----------------- SAUDAÇÃO -----------------
    def saudacao(self, aluno):
        tempo = ano_atual() - aluno["inscrito_ano"]
        print(f'\nOlá, {aluno["nome"]}! Você tem {aluno["idade"]} anos e está conosco há {tempo} anos.\n')

    # ----------------- CARTEIRINHA -----------------
    def carteirinha(self, aluno):
        tempo = ano_atual() - aluno["inscrito_ano"]
        print("===================================")
        print("  CARTEIRINHA - GRUPO LIBERDADE     ")
        print("===================================")
        print(f"ID: {aluno['id']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Apelido: {aluno['apelido']}")
        print(f"Idade: {aluno['idade']} anos")
        print(f"Tempo na capoeira: {tempo} anos")
        print("===================================")

    # ----------------- MOSTRAR ALUNOS -----------------
    def mostrar_alunos(self):
        if not self.data_base:
            print("Nenhum aluno cadastrado.")
            return
        print("\n📋 Alunos cadastrados:")
        for aluno in self.data_base:
            print(f"ID: {aluno['id']} | {aluno['nome']} ({aluno['apelido']})")

    # ----------------- PROCURAR ALUNO -----------------
    def procurar_aluno(self, id_busca):
        for aluno in self.data_base:
            if aluno['id'] == id_busca:
                return aluno
        return None

    # ----------------- EDITAR ALUNO -----------------
    def editar_aluno(self, id_busca):
        aluno = self.procurar_aluno(id_busca)
        if not aluno:
            print("❌ Aluno não encontrado.")
            return

        print("\nDigite os novos dados (pressione Enter para manter o atual):")
        novo_nome = input(f"Nome [{aluno['nome']}]: ") or aluno['nome']
        novo_apelido = input(f"Apelido [{aluno['apelido']}]: ") or aluno['apelido']
        nova_idade = input(f"Idade [{aluno['idade']}]: ")
        nova_idade = int(nova_idade) if nova_idade else aluno['idade']
        novo_ano = input(f"Ano de inscrição [{aluno['inscrito_ano']}]: ")
        novo_ano = int(novo_ano) if novo_ano else aluno['inscrito_ano']

        aluno.update({
            "nome": novo_nome,
            "apelido": novo_apelido,
            "idade": nova_idade,
            "inscrito_ano": novo_ano
        })

        self.salvar_alunos()
        print("✅ Aluno atualizado com sucesso!")

    # ----------------- REMOVER ALUNO -----------------
    def remover_aluno(self, id_busca):
        aluno = self.procurar_aluno(id_busca)
        if not aluno:
            print("❌ Aluno não encontrado.")
            return
        self.data_base.remove(aluno)
        self.salvar_alunos()
        print(f"✅ Aluno {aluno['nome']} removido com sucesso!")
