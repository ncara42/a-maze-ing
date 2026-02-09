RED    = \033[31m
GREEN  = \033[32m
BLUE   = \033[34m
RESET  = \033[0m


VENV   = venv
BIN    = $(VENV)/bin

PYTHON = $(BIN)/python3 -B

all: install

install:
	@echo "$(GREEN)Creando entorno virtual e instalando paquete...$(RESET)"
	@python3 -m venv $(VENV)
	@$(BIN)/pip install --upgrade pip
	@$(BIN)/pip install -r requirements.txt
	@# Instalamos el .whl si existe, si no, instalamos el modo editable
	@if [ -d "dist" ]; then $(BIN)/pip install dist/*.whl; else $(BIN)/pip install -e .; fi

run:
	@./$(BIN)/python3 a_maze_ing.py $(FILENAME)

debug:
	@./$(BIN)/python3 -m pdb a_maze_ing.py $(FILENAME)

help:
	@echo "$(BLUE)=== GUÍA DE INSTALACIÓN DEL PAQUETE (.whl) ===$(RESET)"
	@echo ""
	@echo "$(GREEN)Paso 1: Generar el paquete$(RESET)"
	@echo "  run: 'make package'"
	@echo "  Crea el archivo .whl y lo copia a la raíz del repositorio."
	@echo ""
	@echo "$(GREEN)Paso 2: Crear el entorno virtual (Limpio)$(RESET)"
	@echo "  run: 'python3 -m venv venv && source venv/bin/activate'"
	@echo "  Crea la burbuja aislada para la instalación."
	@echo ""
	@echo "$(GREEN)Paso 3: Instalar el .whl$(RESET)"
	@echo "  run: 'pip install mazegen-*.whl'"
	@echo "  Instala tu generador como una librería del sistema."
	@echo ""
	@echo "$(GREEN)Paso 4: Verificar ejecución$(RESET)"
	@echo "  run: 'amazeing test_input.txt'"
	@echo "  El comando debe funcionar desde cualquier carpeta del venv."
	@echo ""

package:
	@echo "$(BLUE)Building the wheel package...$(RESET)"
	@python3 -m venv temp_build
	@./temp_build/bin/pip install -q build
	@./temp_build/bin/python3 -m build
	@rm -rf temp_build
	@cp dist/*.whl .
	@echo "$(GREEN)Done! Check the 'dist' folder.$(RESET)"

clean:
	@echo "$(RED)Eliminando entorno virtual...$(RESET)"
	@rm -rf $(VENV)
	@rm -rf .mypy_cache build

fclean: clean
	@echo "$(RED)Limpiando todo...$(RESET)"
	@rm -rf dist src/*.egg-info
	@find . -type d -name "__pycache__" -exec rm -rf {} +

lint:
	@echo "$(blue)Testing for flake8 errors...$(reset)"
	@flake8 a_maze_ing.py
	@echo "$(green)No flake8 errors were found$(reset)"
	@echo "$(blue)Testing for mypy errors...$(reset)"
	@mypy a_maze_ing.py --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	@echo "$(blue)Testing for mypy --strict errors...$(reset)"
	@mypy a_maze_ing.py --strict

re: fclean install

.PHONY: all install run package clean fclean re debug
