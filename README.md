# Imersão Engenharia de Software: Dev na Era da IA

Repositório com os desafios e exercícios práticos que desenvolvi durante a **Imersão Engenharia de Software: Dev na Era da IA**, promovida pela **Alura** em parceria com o **Google**.

A imersão aborda práticas de engenharia de software e o uso de inteligência artificial e agentes no processo de desenvolvimento. Os projetos reunidos aqui registram meus estudos de lógica de programação, tratamento de erros, testes automatizados e desenvolvimento web.

🔗 [Página oficial da imersão](https://www.alura.com.br/imersao-engenharia-software-ia-google)

## Desafios

### 1. Calculadora em Python

📁 [`desafio-1.py`](desafio-1.py)

Calculadora de linha de comando com as quatro operações básicas:

- Adição, subtração, multiplicação e divisão;
- Menu interativo para seleção da operação;
- Validação de entradas numéricas;
- Tratamento de divisão por zero.

**Conceitos:** funções, estruturas condicionais, laços de repetição, entrada de dados e tratamento de exceções.

### 2. Calculadora aprimorada e testes automatizados

📁 [`desafio-2/`](desafio-2)

Evolução da calculadora anterior, com:

- Operação adicional de raiz quadrada;
- Exceções para operações inválidas, como divisão por zero e raiz quadrada de número negativo;
- Tratamento de interrupções na interface de linha de comando;
- Testes automatizados com `unittest`, cobrindo diferentes entradas e casos de erro.

**Conceitos:** evolução incremental, validação de comportamento, casos de borda e testes unitários.

### 3. Aplicação web de lista de tarefas

📁 [`desafio-3/`](desafio-3) · 📖 [Documentação do desafio](desafio-3/README.md)

Aplicação de lista de tarefas construída com **HTML, CSS e JavaScript puro**, sem frameworks.

**Funcionalidades:**

- Adicionar, concluir, reabrir e remover tarefas;
- Visualização de tarefas pendentes e concluídas;
- Contadores atualizados automaticamente;
- Persistência dos dados no `localStorage` do navegador;
- Interface responsiva e feedback visual para os diferentes estados.

O diretório também contém testes em Python para verificar a estrutura HTML, regras de CSS, elementos esperados no JavaScript e uma simulação de operações da lista de tarefas. Esses testes não substituem testes de ponta a ponta executados no navegador.

**Conceitos:** manipulação do DOM, eventos, gerenciamento de estado, armazenamento local e organização de código front-end.

## Tecnologias utilizadas

- **Python 3** — lógica de programação, aplicações de terminal e testes;
- **`unittest`** — testes automatizados;
- **HTML5 e CSS3** — estrutura e estilização da aplicação web;
- **JavaScript (Vanilla JS)** — interatividade, DOM e persistência com `localStorage`.

## Estrutura do repositório

```text
├── desafio-1.py
├── desafio-2/
│   ├── calculadora.py
│   └── test_calculadora.py
├── desafio-3/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── test_todo.py
│   └── README.md
└── README.md
```

## Como executar

Clone o repositório e acesse a pasta:

```bash
git clone https://github.com/marcos314159/imersao-alura-dev-na-era-da-ia.git
cd imersao-alura-dev-na-era-da-ia
```

**Desafio 1 — calculadora básica:**

```bash
python desafio-1.py
```

**Desafio 2 — calculadora aprimorada:**

```bash
python desafio-2/calculadora.py
```

**Desafio 3 — lista de tarefas:** abra o arquivo `desafio-3/index.html` em um navegador. Não é necessário instalar dependências ou configurar um servidor.

### Executar os testes

Com Python 3 instalado, utilize o módulo `unittest` da biblioteca padrão:

```bash
python -m unittest discover -s desafio-2 -p "test_*.py"
python -m unittest discover -s desafio-3 -p "test_*.py"
```

## Sobre este repositório

Este repositório tem finalidade **educacional** e reúne exercícios desenvolvidos durante a imersão. Os desafios documentados aqui são projetos independentes, não uma implementação completa de um agente de IA.

**Autor:** [Marcos](https://github.com/marcos314159)