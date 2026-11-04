"""
Testes automatizados para a aplicação de Lista de Tarefas (To-Do List) - Desafio 3.
Verifica integridade de HTML, regras e diferenciação visual no CSS,
e a lógica de funcionamento e renderização do JavaScript.
"""

import unittest
import re
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "index.html"
CSS_FILE = BASE_DIR / "style.css"
JS_FILE = BASE_DIR / "script.js"


class TestHTMLIntegrity(unittest.TestCase):
    """Verifica a integridade e conformidade da estrutura do HTML."""

    @classmethod
    def setUpClass(cls):
        cls.html_content = HTML_FILE.read_text(encoding="utf-8")

    def test_html_file_exists(self):
        self.assertTrue(HTML_FILE.is_file(), "index.html deve existir")

    def test_links_css_and_script(self):
        self.assertIn('href="style.css"', self.html_content, "index.html deve vincular style.css")
        self.assertIn('src="script.js"', self.html_content, "index.html deve vincular script.js")

    def test_required_dom_elements_exist(self):
        required_ids = [
            "task-form",
            "task-input",
            "add-btn",
            "task-counter",
            "completed-counter",
            "task-list",
            "empty-state"
        ]
        for element_id in required_ids:
            with self.subTest(element_id=element_id):
                self.assertIn(
                    f'id="{element_id}"',
                    self.html_content,
                    f"Elemento com id '{element_id}' deve estar presente no HTML"
                )

    def test_input_has_accessibility_and_validation_attributes(self):
        self.assertIn('required', self.html_content, "Input deve possuir o atributo required")
        self.assertIn('placeholder=', self.html_content, "Input deve possuir placeholder orientador")


class TestCSSVisualDistinction(unittest.TestCase):
    """Verifica se os estilos CSS garantem a diferenciação visual entre tarefas concluídas e pendentes."""

    @classmethod
    def setUpClass(cls):
        cls.css_content = CSS_FILE.read_text(encoding="utf-8")

    def test_css_file_exists(self):
        self.assertTrue(CSS_FILE.is_file(), "style.css deve existir")

    def test_variables_defined(self):
        for var in ["--primary-color", "--success-color", "--danger-color", "--text-muted"]:
            with self.subTest(variable=var):
                self.assertIn(var, self.css_content, f"Variável {var} deve estar definida em :root")

    def test_pending_task_item_style(self):
        # Verifica a estilização base do task-item com borda indicativa
        self.assertIn(".task-item {", self.css_content)
        self.assertIn("border-left:", self.css_content)

    def test_completed_task_visual_difference(self):
        # Tarefa concluída deve ter background diferenciado, borda verde, opacidade e texto riscado
        self.assertIn(".task-item.completed", self.css_content)
        self.assertIn("line-through", self.css_content, "Texto de tarefa concluída deve ter line-through")
        self.assertIn("font-style: italic", self.css_content, "Texto de tarefa concluída deve ter font-style: italic")
        self.assertIn("accent-color: var(--success-color)", self.css_content, "Checkbox de concluída deve usar cor de sucesso")

    def test_completed_badge_style(self):
        # Deve haver definição para o badge de identificação visual da tarefa concluída
        self.assertIn(".completed-badge", self.css_content, "Classe .completed-badge deve estar definida no CSS")
        self.assertIn("margin-left: auto", self.css_content, "Badge deve se alinhar à direita antes do botão de excluir")


class TestJavaScriptLogic(unittest.TestCase):
    """
    Testa e valida o modelo de estado e a lógica comportamental do script.js:
    - Adicionar tarefa
    - Alternar conclusão (pendente <-> concluída)
    - Remover tarefa
    - Contadores e regras de singular/plural
    - Serialização com LocalStorage
    """

    def setUp(self):
        # Simulação limpa do estado e ambiente da aplicação
        self.tasks = []
        self.storage = {}

    def _salvar_tarefas(self):
        self.storage["minhas_tarefas_app"] = json.dumps(self.tasks)

    def _carregar_tarefas(self):
        raw = self.storage.get("minhas_tarefas_app")
        if raw:
            try:
                return json.loads(raw)
            except Exception:
                return []
        return []

    def _adicionar_tarefa(self, texto):
        texto = texto.strip()
        if not texto:
            return None
        nova_tarefa = {
            "id": len(self.tasks) + 1,
            "text": texto,
            "completed": False
        }
        self.tasks.insert(0, nova_tarefa)
        self._salvar_tarefas()
        return nova_tarefa

    def _alternar_conclusao(self, task_id):
        self.tasks = [
            {**t, "completed": not t["completed"]} if t["id"] == task_id else t
            for t in self.tasks
        ]
        self._salvar_tarefas()

    def _remover_tarefa(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self._salvar_tarefas()

    def _obter_contadores(self):
        total = len(self.tasks)
        concluidas = len([t for t in self.tasks if t["completed"]])
        total_str = f"{total} {'tarefa' if total == 1 else 'tarefas'} no total"
        concluidas_str = f"{concluidas} concluída{'' if concluidas == 1 else 's'}"
        return total_str, concluidas_str

    def _simular_render(self, task):
        # Simula as classes e elementos gerados pelo renderizar() do script.js
        li_class = f"task-item {'completed' if task['completed'] else 'pending'}"
        badge_rendered = "✓ Concluída" if task["completed"] else None
        return li_class, badge_rendered

    def test_adicionar_tarefa_cria_item_pendente(self):
        tarefa = self._adicionar_tarefa("Estudar JavaScript")
        self.assertIsNotNone(tarefa)
        self.assertEqual(tarefa["text"], "Estudar JavaScript")
        self.assertFalse(tarefa["completed"], "Nova tarefa deve começar como pendente (completed=False)")
        self.assertEqual(len(self.tasks), 1)

    def test_adicionar_tarefa_ignora_texto_vazio(self):
        tarefa = self._adicionar_tarefa("   ")
        self.assertIsNone(tarefa, "Não deve adicionar tarefa com texto em branco")
        self.assertEqual(len(self.tasks), 0)

    def test_alternar_conclusao_muda_status_e_elementos_visuais(self):
        tarefa = self._adicionar_tarefa("Comprar café")
        task_id = tarefa["id"]

        # Inicialmente pendente
        li_class, badge = self._simular_render(self.tasks[0])
        self.assertEqual(li_class, "task-item pending")
        self.assertIsNone(badge, "Tarefa pendente não deve ter badge 'Concluída'")

        # Alterna para concluída
        self._alternar_conclusao(task_id)
        self.assertTrue(self.tasks[0]["completed"])
        li_class, badge = self._simular_render(self.tasks[0])
        self.assertEqual(li_class, "task-item completed")
        self.assertEqual(badge, "✓ Concluída", "Tarefa concluída deve renderizar a badge '✓ Concluída'")

        # Alterna novamente de volta para pendente
        self._alternar_conclusao(task_id)
        self.assertFalse(self.tasks[0]["completed"])
        li_class, badge = self._simular_render(self.tasks[0])
        self.assertEqual(li_class, "task-item pending")
        self.assertIsNone(badge)

    def test_remover_tarefa(self):
        t1 = self._adicionar_tarefa("Tarefa 1")
        t2 = self._adicionar_tarefa("Tarefa 2")
        self.assertEqual(len(self.tasks), 2)

        self._remover_tarefa(t1["id"])
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["id"], t2["id"])

    def test_contadores_singular_e_plural(self):
        # 0 tarefas
        total_str, conc_str = self._obter_contadores()
        self.assertEqual(total_str, "0 tarefas no total")
        self.assertEqual(conc_str, "0 concluídas")

        # 1 tarefa pendente
        t1 = self._adicionar_tarefa("Primeira tarefa")
        total_str, conc_str = self._obter_contadores()
        self.assertEqual(total_str, "1 tarefa no total")
        self.assertEqual(conc_str, "0 concluídas")

        # 1 tarefa concluída
        self._alternar_conclusao(t1["id"])
        total_str, conc_str = self._obter_contadores()
        self.assertEqual(total_str, "1 tarefa no total")
        self.assertEqual(conc_str, "1 concluída")

        # 2 tarefas (1 pendente, 1 concluída)
        t2 = self._adicionar_tarefa("Segunda tarefa")
        total_str, conc_str = self._obter_contadores()
        self.assertEqual(total_str, "2 tarefas no total")
        self.assertEqual(conc_str, "1 concluída")

        # 2 tarefas concluídas
        self._alternar_conclusao(t2["id"])
        total_str, conc_str = self._obter_contadores()
        self.assertEqual(total_str, "2 tarefas no total")
        self.assertEqual(conc_str, "2 concluídas")

    def test_persistencia_localstorage(self):
        self._adicionar_tarefa("Persistir dados")
        self.assertIn("minhas_tarefas_app", self.storage)
        
        # Recupera dados salvos
        tarefas_carregadas = self._carregar_tarefas()
        self.assertEqual(len(tarefas_carregadas), 1)
        self.assertEqual(tarefas_carregadas[0]["text"], "Persistir dados")
        self.assertFalse(tarefas_carregadas[0]["completed"])


class TestScriptSourceConsistency(unittest.TestCase):
    """Garante que script.js contém todos os handlers e seletores correspondentes ao index.html e style.css."""

    @classmethod
    def setUpClass(cls):
        cls.js_content = JS_FILE.read_text(encoding="utf-8")

    def test_js_selectors_match_html(self):
        expected_ids = [
            "task-form",
            "task-input",
            "task-list",
            "empty-state",
            "task-counter",
            "completed-counter"
        ]
        for element_id in expected_ids:
            with self.subTest(element_id=element_id):
                self.assertIn(
                    f'document.getElementById("{element_id}")',
                    self.js_content,
                    f"script.js deve selecionar o elemento id '{element_id}'"
                )

    def test_js_creates_completed_and_pending_classes(self):
        # Verifica se o script aplica as classes que o CSS estiliza
        self.assertIn('task.completed ? "completed" : "pending"', self.js_content)
        self.assertIn('completed-badge', self.js_content)
        self.assertIn('✓ Concluída', self.js_content)

    def test_js_functions_exist(self):
        functions = [
            "carregarTarefasSalvas",
            "salvarTarefas",
            "adicionarTarefa",
            "alternarConclusao",
            "removerTarefa",
            "atualizarContadores",
            "renderizar"
        ]
        for fn in functions:
            with self.subTest(function=fn):
                pattern = rf"function\s+{fn}\s*\("
                self.assertTrue(
                    re.search(pattern, self.js_content),
                    f"A função '{fn}' deve estar declarada no script.js"
                )


if __name__ == "__main__":
    unittest.main()
