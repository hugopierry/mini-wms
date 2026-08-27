# 📦 Mini WMS — Python

Sistema de gerenciamento de estoque desenvolvido em **Python**, criado como um **laboratório de estudos práticos**.

O projeto acompanha minha evolução nos estudos de **Python, Programação Orientada a Objetos (POO), SQL, SQLite, banco de dados, Git e GitHub**.

A ideia é simples: aprender um conceito e colocá-lo em prática diretamente no projeto.

---

## 📌 Sobre o projeto

O **Mini WMS** é um projeto pessoal inspirado em sistemas de gerenciamento de estoque.

Ele começou como uma aplicação simples executada pelo terminal e vem evoluindo conforme avanço nos estudos.

Atualmente, o projeto possui:

* 🔐 Sistema de autenticação de usuários
* 📦 Gerenciamento de produtos
* 🗄️ Persistência de dados utilizando SQLite
* 🔎 Consultas e manipulação de dados com SQL
* 🧩 Organização do código em módulos
* 📝 Versionamento utilizando Git e GitHub

O projeto está em desenvolvimento contínuo e novas funcionalidades serão adicionadas conforme novos conhecimentos forem sendo aplicados.

---

## ⚙️ Funcionalidades

### 🔐 Usuários

* Criar usuário
* Criar senha
* Cadastrar nome completo
* Validar usuário
* Validar senha
* Menu de login
* Persistência dos usuários no SQLite
* Tratamento de matrícula duplicada
* Senha oculta durante a digitação

### 📦 Produtos

* Cadastro de produtos
* Código de barras
* SKU
* Descrição
* Caixaria
* Validade
* Lote
* Quantidade
* Valor unitário
* Inserção de produtos no banco de dados
* Consulta de produtos utilizando SQL

---

## 🗄️ Banco de dados

O projeto utiliza **SQLite** para armazenar os dados.

### Tabela `usuarios`

```text
usuarios
├── matricula
├── senha
└── nome
```

### Tabela `produtos`

```text
produtos
├── id
├── codigo_barras
├── sku
├── descricao
├── caixaria
├── validade
├── lote
├── quantidade
└── valor_unitario
```

---

## 🧪 Laboratório de estudos

O Mini WMS também funciona como um ambiente para colocar em prática os conhecimentos adquiridos durante meus estudos.

Entre os conceitos praticados estão:

* Python
* POO
* SQL
* SQLite
* CRUD
* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`
* Funções de agregação como `MAX()` e `MIN()`
* Tratamento de erros
* Organização de projetos
* Git e GitHub

---

## 🚧 Em desenvolvimento

O projeto continua sendo desenvolvido gradualmente.

Novos conhecimentos aprendidos durante os estudos serão aplicados diretamente no Mini WMS, mantendo o projeto em constante evolução.

**Aprender → aplicar → errar → corrigir → versionar → evoluir.** 🚀
