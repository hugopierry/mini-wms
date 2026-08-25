# 📦 Mini WMS — Python

Sistema de gerenciamento de estoque desenvolvido em **Python**, criado com o objetivo de praticar e aplicar conceitos de **Programação Orientada a Objetos (POO)**, **SQL**, **SQLite** e organização de projetos em módulos.

O projeto está sendo desenvolvido gradualmente conforme avanço nos estudos de Python, POO e bancos de dados.

---

## 📌 Sobre o projeto

O **Mini WMS** é um projeto de estudo inspirado em sistemas de gerenciamento de estoque.

A aplicação possui um sistema de autenticação de usuários e um módulo de gerenciamento de produtos, permitindo realizar operações básicas de estoque através de um menu interativo no terminal.

Atualmente, o sistema de usuários já possui persistência utilizando **SQLite**.

A próxima etapa do projeto é integrar também o gerenciamento de produtos ao banco de dados.

---

## ⚙️ Funcionalidades

### 🔐 Usuários

- [x] Criar usuário
- [x] Criar senha
- [x] Cadastrar nome completo
- [x] Validar senha
- [x] Validar usuário
- [x] Menu de login
- [x] Persistência de usuários com SQLite
- [x] Tratamento de matrícula duplicada
- [x] Senha oculta durante a digitação

### 📦 Estoque

- [x] Cadastro de produtos em memória
- [x] Entrada de produtos
- [x] Retirada de produtos
- [x] Listagem de produtos
- [ ] Persistência dos produtos no SQLite
- [ ] Cadastro de produtos integrado ao banco
- [ ] Entrada integrada ao banco
- [ ] Retirada integrada ao banco
- [ ] Listagem integrada ao banco

---

## 🗄️ Banco de dados

O projeto utiliza **SQLite** para persistência dos dados.

### Tabela de usuários

Atualmente o sistema possui a tabela:

```text
usuarios
├── matricula
├── senha
└── nome