# 🥋 Sistema de Gerenciamento do Grupo de Capoeira Liberdade

Este projeto é um **sistema em Python para cadastro e gerenciamento de alunos de um grupo de capoeira**, utilizando estrutura modularizada, persistência em arquivo JSON e execução via terminal.

> ✅ Esta versão do projeto **não utiliza interface gráfica (GUI)** — todo o sistema funciona via terminal.

---

## 🚀 Funcionalidades

* ✅ Cadastro de alunos
* ✅ Geração de ID único automático
* ✅ Listagem de alunos cadastrados
* ✅ Geração de carteirinha por ID
* ✅ Edição de dados do aluno
* ✅ Remoção de alunos
* ✅ Persistência de dados em arquivo `data.json`
* ✅ Sistema modularizado

---

## 🗂 Estrutura do Projeto

```
grupo_capoeira/
│
├── main.py          # Arquivo principal (menu do sistema)
├── alunos.py        # Classe GrupoCapoeira (regras do sistema)
├── utils.py         # Funções auxiliares (UUID e data)
└── data.json        # Banco de dados dos alunos
```

---

## ⚙️ Requisitos

* Python 3.10 ou superior
* Biblioteca padrão (`uuid`, `json`, `datetime`)

Nenhuma biblioteca externa é necessária.

---

## ▶️ Como Executar

### 1️⃣ Entrar na pasta do projeto

```bash
cd grupo_capoeira
```

### 2️⃣ Executar o sistema

```bash
python main.py
```

Ou, se estiver no Linux:

```bash
chmod +x main.py
./main.py
```

---

## 📋 Menu do Sistema

Ao iniciar o programa, você verá o seguinte menu:

```
==== SISTEMA DE GERENCIAMENTO DO GRUPO DE CAPOEIRA LIBERDADE ====

1. Cadastrar aluno
2. Listar alunos
3. Gerar carteirinha por ID
4. Editar aluno
5. Remover aluno
0. Sair
```

---

## 💾 Banco de Dados (`data.json`)

O arquivo `data.json` armazena todos os alunos cadastrados, exemplo:

```json
[
    {
        "id": "c0b3b7a2-3f10-4f38-8f18-fd5a9a9b1234",
        "nome": "João Silva",
        "apelido": "Joãozinho",
        "idade": 25,
        "inscrito_ano": 2020
    }
]
```

> ⚠️ **Nunca apague o `data.json` se quiser manter os dados salvos.**

---

## 🛠 Tecnologias Usadas

* Python 3
* Programação Orientada a Objetos (POO)
* Manipulação de arquivos JSON
* UUID para geração de ID único
* Estrutura modular

---

## 📌 Objetivo do Projeto

Este sistema foi desenvolvido para:

* Organizar alunos de um grupo de capoeira
* Automatizar a geração de carteirinhas
* Servir como projeto prático de estudo em Python
* Aplicar conceitos de modularização, POO e persistência de dados

---

## ✅ Próximas Possíveis Evoluções

* Geração de carteirinha em PDF
* QR Code para validação do aluno
* Interface gráfica
* Integração com banco de dados real (SQLite ou PostgreSQL)
* Sistema de presença nas aulas

---

## 👨‍💻 Autor

Projeto desenvolvido por **Wallace José** como parte de estudos em programação Python e automação de sistemas.

---

✅ Sistema pronto para uso em ambiente real de grupo de capoeira.

---

## ⚡ Execução em Uma Única Linha (Para Usuários)

Use um dos comandos abaixo para **clonar, preparar o ambiente e executar o sistema automaticamente**.

### ✅ Linux / Mac (uma linha)

```bash
git clone https://github.com/Cranio2002/testes_mk1.git && cd testes_mk1 && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python main.py
```

### ✅ Windows (uma linha)

```bat
git clone https://github.com/Cranio2002/testes_mk1.git && cd testes_mk1 && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python main.py
```

✅ Esses comandos já fazem automaticamente:

* Clone do repositório
* Criação e ativação do ambiente virtual
* Instalação das dependências
* Execução do sistema
