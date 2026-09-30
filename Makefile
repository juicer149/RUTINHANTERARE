PYTHON := python3

.PHONY: help compile test check run

help:
	@echo "RUTINHANTERARE commands"
	@echo ""
	@echo "  make run       Run the interactive program"
	@echo "  make compile   Compile Python files"
	@echo "  make test      Run unit tests"
	@echo "  make check     Run compile + tests"

run:
	$(PYTHON) main.py

compile:
	$(PYTHON) -m compileall -q .

test:
	$(PYTHON) -m unittest discover -v

check: compile test
