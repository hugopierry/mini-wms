# 📦 Mini WMS

Sistema de gerenciamento de estoque desenvolvido em **Python**, criado inicialmente como um projeto de aprendizado e prática de programação.

O projeto começou de forma simples, armazenando os dados principalmente **em memória RAM** e utilizando alguns arquivos de texto para determinadas informações. Conforme avancei nos estudos, percebi a necessidade de tornar a aplicação mais organizada, persistente e próxima de um sistema utilizado em um ambiente real.

A partir disso, iniciei o estudo e a implementação de **SQL e banco de dados**, aplicando os conhecimentos diretamente no projeto e realizando melhorias de forma incremental.

---

## 🚀 Evolução do projeto

O Mini WMS passou por diversas etapas de desenvolvimento.

### 🟢 Primeira versão

Inicialmente, o sistema trabalhava principalmente com dados armazenados em **memória RAM**.

Algumas informações também eram armazenadas em arquivos de texto, funcionando como uma solução simples para os primeiros testes.

O objetivo nessa etapa era principalmente praticar:

* Python
* Classes e objetos
* Estruturas de dados
* Funções
* Lógica de programação
* Manipulação de estoque

---

### 🟡 Implementação do banco de dados

Com a evolução dos estudos, comecei a estudar a aplicação de **SQL e bancos de dados** para melhorar a estrutura do sistema.

A partir disso, o projeto passou a utilizar **SQLite**, permitindo que os dados do estoque fossem armazenados de forma persistente.

Com essa mudança, foram implementadas operações de banco de dados para:

* Cadastro de produtos
* Entrada de produtos
* Retirada de produtos
* Consulta de produtos
* Atualização de estoque
* Persistência dos dados

Essa etapa foi importante para transformar o projeto de um simples exercício em uma aplicação mais estruturada.

---

## 🔐 Evolução do sistema de login

O sistema de autenticação também passou por várias etapas.

### Primeira versão

Inicialmente, o login era simples, utilizando **usuário e senha previamente definidos no código**.

### Cadastro de usuários

Posteriormente, o sistema passou a permitir a criação de usuários de forma mais dinâmica.

O usuário pode informar:

* Matrícula
* Senha
* Confirmação da senha
* Nome

O sistema também realiza uma validação para verificar se a senha informada é igual à senha de confirmação.

### 🔒 Login com validação de acesso

Com a evolução do projeto, o login passou a consultar os usuários cadastrados no banco de dados e validar as credenciais antes de permitir o acesso ao sistema.

O fluxo passou a contar com:

* 🔐 Entrar no sistema
* 👤 Criar usuário
* 🚪 Sair
* ✅ Validação de usuário e senha
* ❌ Bloqueio de acesso quando as credenciais são incorretas

---

## 🧭 Separação do acesso e do menu do WMS

Anteriormente, o login e as funções do sistema estavam integrados em um único menu.

Essa estrutura foi modificada para separar as responsabilidades.

Atualmente, o fluxo funciona da seguinte forma:

**Login → Validação de acesso → Menu principal do WMS**

Somente após uma autenticação válida o usuário consegue acessar as funções de gerenciamento do estoque.

### Menu do WMS

Após o login, o usuário pode acessar:

```text
1 - Cadastrar produto
2 - Inserir produto
3 - Retirar produto
4 - Listar produto
0 - Sair
```

Dessa forma, as operações de estoque ficam protegidas pelo processo de autenticação.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **SQLite**
* **SQL**
* **Rich**
* **pwinput**
* **Git**
* **GitHub**

---

## 📚 Objetivo do projeto

O Mini WMS é, principalmente, um **laboratório de aprendizado**.

A proposta é estudar novos conceitos e aplicá-los diretamente em um projeto prático, observando como uma aplicação simples pode evoluir gradualmente para uma estrutura mais organizada.

Durante o desenvolvimento, novas ideias de melhoria são registradas, estudadas e posteriormente aplicadas ao sistema.

Por isso, este README também será atualizado conforme o projeto evoluir.

---

## 🔄 Projeto em evolução

O desenvolvimento do Mini WMS é contínuo.

Novas funcionalidades, melhorias na estrutura do código, banco de dados, autenticação, interface e organização do projeto serão adicionadas conforme novos conhecimentos forem adquiridos.

**O objetivo não é apenas criar um sistema de estoque, mas utilizar o projeto como uma forma prática de aprender, testar e consolidar conhecimentos em desenvolvimento de software.**
