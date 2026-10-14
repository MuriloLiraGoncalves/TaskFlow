# TaskFlow — Gerenciador de Tarefas Acadêmicas

O **TaskFlow** é uma aplicação web desenvolvida em Python e Django para auxiliar estudantes na organização de suas atividades acadêmicas. O projeto foi desenvolvido como estudo prático de arquitetura de software, com foco na separação de responsabilidades e nos conceitos relacionados ao padrão MVC.

## Objetivos

- Organizar tarefas acadêmicas em um único lugar.
- Permitir o cadastro e a visualização de tarefas.
- Registrar descrições e prazos.
- Marcar tarefas como concluídas ou reabri-las.
- Excluir tarefas cadastradas.
- Demonstrar a organização de uma aplicação web em componentes com responsabilidades distintas.

## Tecnologias utilizadas

- **Python:** linguagem de programação.
- **Django:** framework web utilizado no desenvolvimento do sistema.
- **SQLite:** banco de dados utilizado na configuração inicial do projeto.
- **HTML e CSS:** estrutura e apresentação da interface.
- **Visual Studio Code:** ambiente de desenvolvimento.

## Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| Cadastro | Permite adicionar tarefas com título, descrição e prazo opcional. |
| Listagem | Exibe as tarefas cadastradas. |
| Conclusão | Permite marcar tarefas como concluídas. |
| Reabertura | Permite retornar uma tarefa ao estado pendente. |
| Exclusão | Permite remover tarefas cadastradas. |

## Arquitetura do projeto

O Django utiliza oficialmente o padrão **MTV (Model–Template–View)**. Para fins didáticos, sua organização pode ser relacionada conceitualmente ao MVC tradicional.

- **Model:** `tarefas/models.py` define a estrutura e a persistência dos dados.
- **View/Controller, em sentido conceitual:** `tarefas/views.py` contém as funções que recebem as requisições e coordenam as operações.
- **Template:** `tarefas/templates/tarefas/lista.html` apresenta o formulário e as tarefas ao usuário.
- **Rotas:** `tarefas/urls.py` e `config/urls.py` direcionam as requisições para as funções correspondentes.
- **Formulário:** `tarefas/forms.py` define os campos e a validação do cadastro.

### Estrutura de diretórios

```text
taskflow/
├── config/
│   ├── settings.py
│   └── urls.py
├── tarefas/
│   ├── migrations/
│   ├── templates/
│   │   └── tarefas/
│   │       └── lista.html
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── README.md
```

*Observação: a estrutura acima destaca os arquivos principais do projeto. Outros arquivos padrão do Django também podem estar presentes.*

## Como executar o projeto

### 1. Pré-requisitos

- Python instalado.
- pip disponível no ambiente Python.
- Terminal e Visual Studio Code ou outro editor de sua preferência.

### 2. Clonar o repositório

Caso o projeto esteja publicado no GitHub:

```bash
git clone URL_DO_REPOSITORIO
cd taskflow
```

Se o projeto ainda estiver apenas no computador, abra o terminal na pasta que contém o arquivo `manage.py`.

### 3. Criar e ativar o ambiente virtual

No Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar o Django

```powershell
python -m pip install django
```

### 5. Preparar o banco de dados

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 6. Iniciar o servidor

```powershell
python manage.py runserver
```

Acesse a aplicação no navegador:

http://127.0.0.1:8000/

Para interromper o servidor, pressione `Ctrl + C` no terminal.

## Testes automatizados

O projeto contém testes automatizados em `tarefas/tests.py` para verificar o carregamento da página inicial, o cadastro, a conclusão e a exclusão de tarefas.

Para executar os testes:

```powershell
python manage.py test tarefas
```

O resultado deverá ser analisado no terminal. Os testes só devem ser considerados aprovados quando a execução terminar sem falhas.

## Limitações e melhorias futuras

Entre as melhorias que podem ser implementadas em versões futuras estão:

- Autenticação e contas individuais para estudantes.
- Filtros por prazo e status.
- Edição de tarefas.
- Interface responsiva aprimorada.
- Proteção das ações de alteração e exclusão por métodos HTTP e controles de acesso adequados.
- Publicação da aplicação em um serviço de hospedagem.

## Finalidade acadêmica

O TaskFlow foi concebido como projeto prático para estudar arquitetura de software, organização do código, persistência de dados, tratamento de requisições e apresentação de informações em aplicações web.

A análise acadêmica deve considerar as diferenças entre o MVC tradicional e o MTV utilizado pelo Django, relacionando a implementação às vantagens e limitações da separação de responsabilidades.

---

**Projeto:** TaskFlow — Gerenciador de Tarefas Acadêmicas  
**Linguagem:** Python  
**Framework:** Django  
**Banco de dados:** SQLite