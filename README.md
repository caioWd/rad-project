# Relatório - RAD

## Projeto: Sistema de Administração da Academia de Cross Training (CrossX)

**Disciplina**: Desenvolvimento Rápido de Aplicações em Python
**Professor(a)**: Cynthia Moreira Maia  
**Equipe**: Caio Wendel, Ingrid Araújo e Pedro Arthur

---

## 1. Link repositório FRONT-END

Repositório Front-End: https://github.com/mrsingrid/crossx-frontend/tree/main.

## 1. Planejamento de Requisitos

Nesta fase, a equipe foi reunida para entender os objetivos principais do sistema. Os recursos da API foram definidos com base no briefing fornecido, o qual já continha a análise do sistema. Os requisitos principais identificados foram:

- Cadastro completo de alunos (com informações de contato).
- Controle de matrícula (data de matrícula, vencimento e desligamento).
- Registro e consulta de pagamentos realizados por alunos.

---

## 2. Design do Sistema

Dividimos o projeto em tarefas no **Trello**, organizando por módulos (CRUD de usuário, CRUD de pagamento, regras de matrícula e vencimento).  
O design foi pensado de forma modular, permitindo o desenvolvimento paralelo entre membros da equipe.

A estrutura da aplicação foi baseada no padrão MVC simplificado:

- `models/` — Definição das entidades e acesso ao banco.
- `services/` — Regras de negócio e validações.
- `controllers/` — Camada responsável por receber e retornar as requisições da API.

---

## 3. Construção Rápida

Com os requisitos definidos, partimos para o desenvolvimento:

- **Back-end**: Desenvolvido com **Flask**, seguindo boas práticas de organização de código e tratamento de exceções.

---

## 4. Testes

Os testes foram feitos manualmente utilizando o **Postman** (e também com o Thunder Client, conforme sugestão da professora).

Testamos:

- Todas as rotas da API (usuários, matrículas e pagamentos).
- Regras de negócio (ex: não excluir aluno ativo).
- Validação de entradas e respostas esperadas.

---

## 5. Entrega e Implantação

Após os testes, o sistema foi integrado com o front-end e preparado para entrega.

---

## Conclusão

Seguimos o modelo **RAD** para garantir uma entrega rápida, iterativa e com feedback constante.  
O uso de ferramentas como **Trello**, **Postman** e a divisão em etapas bem definidas contribuíram para a organização e eficiência no desenvolvimento do sistema **CrossX**.
