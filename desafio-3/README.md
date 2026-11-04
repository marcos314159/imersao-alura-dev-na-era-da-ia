# 📋 Aplicação de Lista de Tarefas (To-Do List)

Esta é uma aplicação web simples, visual e didática para gerenciar tarefas diárias. Ela foi criada com o trio fundamental do desenvolvimento web: **HTML5**, **CSS3** e **JavaScript puro (Vanilla JS)**.

---

## 🎯 Funcionalidades

- **Adicionar tarefas:** Digite o nome da atividade e pressione `Enter` ou clique no botão **Adicionar**.
- **Concluir tarefas:** Clique na caixa de seleção (checkbox) ou no texto da tarefa para marcá-la como concluída (com indicador visual verde, etiqueta "✓ Concluída", texto riscado em itálico e mudança de borda).
- **Remover tarefas:** Clique no ícone de lixeira (🗑️) para apagar a tarefa selecionada.
- **Contador automático:** Exibe o total de tarefas e quantas já foram finalizadas.
- **Persistência de dados:** As tarefas são salvas no `LocalStorage` do navegador, ou seja, elas não somem quando a página for recarregada.

---

## 📂 Estrutura do Projeto

O projeto é separado de acordo com os 3 pilares fundamentais da web:

```text
imersao-alura-desafio-3/
├── index.html       # Estrutura e marcação dos elementos
├── style.css        # Visual, cores, tipografia e espaçamento
├── script.js        # Lógica, interatividade e armazenamento
├── test_todo.py     # Testes automatizados de estrutura e comportamento
└── README.md        # Documentação e guia explicativo
```

### 1. `index.html` (A Estrutura)
Responsável por definir **o que existe na tela**:
- Um cabeçalho com título;
- Um formulário com campo de texto e botão de adicionar;
- Uma barra de resumo com contadores;
- Uma lista (`<ul>`) onde os itens criados são inseridos.

### 2. `style.css` (A Aparência)
Responsável por definir **como as coisas se parecem**:
- Cores modernas com suporte a variáveis CSS (`--primary-color`, `--bg-color`, etc.);
- Alinhamento centralizado com `Flexbox`;
- Efeitos visuais suaves de foco, hover e estilo tachado (riscado) para itens concluídos.

### 3. `script.js` (O Comportamento)
Responsável por fazer as coisas **funcionarem**:
- **DOM (Document Object Model):** Seleciona e manipula os elementos HTML em tempo real;
- **Estado (State):** Mantém a lista de tarefas em um array de objetos `[{ id, text, completed }]`;
- **Eventos:** Ouve ações do usuário (clique no botão, envio do formulário, marcação de checkbox);
- **LocalStorage:** Salva e recupera as tarefas no próprio navegador usando `JSON.stringify` e `JSON.parse`.

---

## 🧪 Como Executar os Testes

Para rodar a suíte completa de testes automatizados:

```bash
pytest desafio-3/test_todo.py -v
```

Ou para rodar todos os testes do projeto:

```bash
pytest -v
```

Por ser uma aplicação baseada em tecnologias padrão da web, você **não precisa instalar nada**:

1. Dê um duplo clique no arquivo [`index.html`](file:///home/marcos_mmelo3141/imersao-alura-desafio-3/index.html) para abri-lo diretamente em qualquer navegador (Google Chrome, Firefox, Edge, Safari);
2. Ou, se preferir usar um servidor local com Python (caso tenha instalado):
   ```bash
   python3 -m http.server 8000
   ```
   E acesse `http://localhost:8000` no seu navegador.
