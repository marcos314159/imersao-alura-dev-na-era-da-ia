/**
 * ============================================================================
 * APLICAÇÃO DE LISTA DE TAREFAS (TO-DO LIST)
 * ============================================================================
 * 
 * Este arquivo contém a lógica (comportamento) do nosso aplicativo.
 * Ele é organizado em 4 partes principais:
 * 1. Seleção dos elementos do HTML (DOM)
 * 2. Estado da aplicação (os dados das tarefas)
 * 3. Funções de manipulação (Adicionar, Concluir, Remover, Renderizar)
 * 4. Eventos (ouvintes de cliques e submissão)
 */

// ----------------------------------------------------------------------------
// 1. SELEÇÃO DOS ELEMENTOS DO HTML (DOM)
// ----------------------------------------------------------------------------
const taskForm = document.getElementById("task-form");
const taskInput = document.getElementById("task-input");
const taskList = document.getElementById("task-list");
const emptyState = document.getElementById("empty-state");
const taskCounter = document.getElementById("task-counter");
const completedCounter = document.getElementById("completed-counter");

// Chave utilizada para salvar no LocalStorage do navegador
const STORAGE_KEY = "minhas_tarefas_app";

// ----------------------------------------------------------------------------
// 2. ESTADO DA APLICAÇÃO (DADOS)
// ----------------------------------------------------------------------------
// Tentamos carregar as tarefas já salvas no navegador. Se não houver nenhuma, iniciamos com lista vazia [].
let tasks = carregarTarefasSalvas();

// ----------------------------------------------------------------------------
// 3. FUNÇÕES PRINCIPAIS
// ----------------------------------------------------------------------------

/**
 * Carrega a lista de tarefas salva no LocalStorage.
 * LocalStorage armazena dados em formato de texto (string), por isso usamos JSON.parse().
 */
function carregarTarefasSalvas() {
  const dadosSalvos = localStorage.getItem(STORAGE_KEY);
  if (dadosSalvos) {
    try {
      return JSON.parse(dadosSalvos);
    } catch (e) {
      console.error("Erro ao ler tarefas salvas:", e);
      return [];
    }
  }
  return [];
}

/**
 * Salva a lista de tarefas atual no LocalStorage do navegador.
 * Convertemos a lista de objetos JavaScript em texto com JSON.stringify().
 */
function salvarTarefas() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

/**
 * Adiciona uma nova tarefa à lista.
 * Cada tarefa é um objeto com: id (único), text (descrição) e completed (booleano).
 */
function adicionarTarefa(texto) {
  const novaTarefa = {
    id: Date.now(), // Gera um identificador único baseado no milissegundo atual
    text: texto,
    completed: false
  };

  // Adiciona a nova tarefa no início do array
  tasks.unshift(novaTarefa);

  // Salva e atualiza o visual da tela
  salvarTarefas();
  renderizar();
}

/**
 * Alterna o estado de conclusão de uma tarefa (concluída <-> pendente).
 */
function alternarConclusao(id) {
  // Procura a tarefa pelo ID e inverte o status de 'completed'
  tasks = tasks.map((task) => {
    if (task.id === id) {
      return { ...task, completed: !task.completed };
    }
    return task;
  });

  salvarTarefas();
  renderizar();
}

/**
 * Remove uma tarefa da lista pelo ID.
 */
function removerTarefa(id) {
  // Filtra a lista, mantendo apenas as tarefas cujo ID seja diferente do ID a ser removido
  tasks = tasks.filter((task) => task.id !== id);

  salvarTarefas();
  renderizar();
}

/**
 * Atualiza os contadores de tarefas exibidos na interface.
 */
function atualizarContadores() {
  const total = tasks.length;
  const concluidas = tasks.filter((t) => t.completed).length;

  taskCounter.textContent = `${total} ${total === 1 ? "tarefa" : "tarefas"} no total`;
  completedCounter.textContent = `${concluidas} concluída${concluidas === 1 ? "" : "s"}`;
}

/**
 * Renderiza (desenha) as tarefas na tela criando elementos HTML dinamicamente.
 */
function renderizar() {
  // Limpa o conteúdo atual da lista
  taskList.innerHTML = "";

  // Se não houver tarefas, exibe a mensagem de estado vazio
  if (tasks.length === 0) {
    emptyState.style.display = "block";
  } else {
    emptyState.style.display = "none";

    // Para cada tarefa no array, cria os elementos visuais
    tasks.forEach((task) => {
      // 1. Cria o item da lista <li> com classe condicional
      const li = document.createElement("li");
      li.className = `task-item ${task.completed ? "completed" : "pending"}`;

      // 2. Cria a área de conteúdo (checkbox + texto + badge de status)
      const contentDiv = document.createElement("div");
      contentDiv.className = "task-content";

      // Checkbox para marcar como concluída
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.className = "task-checkbox";
      checkbox.checked = task.completed;
      checkbox.addEventListener("change", () => alternarConclusao(task.id));

      // Texto da tarefa
      const span = document.createElement("span");
      span.className = "task-text";
      span.textContent = task.text;

      // Clicar no texto também alterna a conclusão da tarefa
      span.addEventListener("click", () => alternarConclusao(task.id));

      contentDiv.appendChild(checkbox);
      contentDiv.appendChild(span);

      // Badge visual de status para identificar tarefas concluídas
      if (task.completed) {
        const badge = document.createElement("span");
        badge.className = "task-badge completed-badge";
        badge.textContent = "✓ Concluída";
        badge.title = "Clique para reabrir tarefa";
        badge.addEventListener("click", () => alternarConclusao(task.id));
        contentDiv.appendChild(badge);
      }

      // 3. Cria o botão de exclusão
      const deleteBtn = document.createElement("button");
      deleteBtn.className = "delete-btn";
      deleteBtn.innerHTML = "🗑️";
      deleteBtn.title = "Excluir tarefa";
      deleteBtn.setAttribute("aria-label", "Excluir tarefa");
      deleteBtn.addEventListener("click", () => removerTarefa(task.id));

      // 4. Junta tudo dentro do <li> e insere na lista <ul>
      li.appendChild(contentDiv);
      li.appendChild(deleteBtn);
      taskList.appendChild(li);
    });
  }

  // Atualiza os contadores na barra superior
  atualizarContadores();
}

// ----------------------------------------------------------------------------
// 4. EVENTOS (INTERAÇÕES DO USUÁRIO)
// ----------------------------------------------------------------------------

// Evento disparado ao enviar o formulário (clicar em 'Adicionar' ou pressionar 'Enter')
taskForm.addEventListener("submit", (event) => {
  event.preventDefault(); // Evita o recarregamento padrão da página

  const texto = taskInput.value.trim();

  // Se o campo não estiver vazio, adiciona a tarefa
  if (texto !== "") {
    adicionarTarefa(texto);
    taskInput.value = ""; // Limpa o campo de digitação
    taskInput.focus();    // Mantém o cursor pronto para a próxima tarefa
  }
});

// Renderização inicial assim que o arquivo é carregado
renderizar();
