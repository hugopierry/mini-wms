# Mini WMS

Projeto inspirado no sistema que utilizo no meu trabalho na área de logística, desenvolvido com **dados fictícios** para fins de estudo e aprendizado.

O projeto começou de uma forma bem simples: utilizando o **Bloco de Notas para salvar os dados**. Conforme fui evoluindo nos estudos, percebi uma limitação importante: os dados ficavam apenas na memória RAM e eram perdidos quando o programa era fechado.

A partir disso, evoluí o projeto para utilizar **SQL como banco de dados**, permitindo que as informações fossem armazenadas de forma persistente e utilizadas novamente sempre que o sistema fosse executado.

O Mini WMS é desenvolvido em **Python**, utilizando **SQL/SQLite como banco de dados**. Atualmente, o projeto também está sendo utilizado como um laboratório prático para meus estudos de **Pandas e análise de dados**.

A ideia é que cada aprendizado seja aplicado diretamente nos dados do próprio sistema, em vez de ficar apenas em exercícios isolados.

## Estrutura do projeto

Cada arquivo possui uma responsabilidade específica dentro do sistema:

1. `produto.py` → operações relacionadas aos produtos

2. `estoque.py` → operações relacionadas ao estoque

3. `movimentacao.py` → movimentações de estoque

4. `banco.py` → conexão e operações com o banco de dados

5. `login_oficial.py` → autenticação dos usuários

6. `relatorios.py` → laboratório prático de Pandas e análise dos dados

7. `mini_wms.db` → banco de dados SQLite com os dados utilizados pelo sistema

8. `README.md` → documentação do projeto

## `relatorios.py` — Laboratório de Pandas

O arquivo `relatorios.py` foi criado para funcionar como um **laboratório prático de aprendizado**.

Nele, utilizo os dados do banco de dados do Mini WMS para aprender e aplicar recursos do Python e da biblioteca Pandas.

A ideia é manter registrados no próprio projeto os aprendizados, funções estudadas e exercícios realizados.

O processo de aprendizado segue uma lógica simples:

**Aprender → testar → aplicar → errar → entender o erro → corrigir → aplicar novamente.**

Dessa forma, os erros também fazem parte do processo e ajudam a entender melhor o que está sendo desenvolvido.

Cada novo conhecimento é aplicado diretamente nos dados do Mini WMS, permitindo que a teoria seja transformada em prática.

Até o momento, estou utilizando o arquivo para praticar conceitos como:

* leitura de dados do SQLite com Pandas;
* inspeção e análise de DataFrames;
* tipos de dados;
* identificação de dados duplicados;
* filtros de dados;
* utilização do `loc[]`;
* aplicação de condições simples e compostas;
* seleção de linhas e colunas;
* análise dos dados de estoque.

Os exercícios realizados também ficam registrados no `relatorios.py`, servindo como um histórico da minha evolução durante o desenvolvimento do projeto.

## Objetivo do projeto

O Mini WMS não tem como objetivo ser um sistema WMS completo e pronto para produção.

Ele funciona principalmente como um **laboratório de aprendizado**, no qual consigo unir conhecimentos de:

**Python → SQL → Pandas → análise de dados**

e aplicar esses conhecimentos em um projeto relacionado à área de logística que já conheço na prática.

Com isso, o projeto vai evoluindo junto com meus estudos, enquanto mantenho registrados os conceitos que estou aprendendo e colocando em prática.
