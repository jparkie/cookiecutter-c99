BUILD_DIR = build

TEST_DIR = test

DOCKER_BASE = docker run \
	--volume $$(pwd):/repo \
	--volume /var/run/docker.sock:/var/run/docker.sock \
	--volume $(HOME)/.conan:/root/.conan \
	--net host

DOCKER_RUN_C99 = $(DOCKER_BASE) \
	cookiecutter_c99

DOCKER_RUN_PY36 = $(DOCKER_BASE) \
	cookiecutter_py36

DOCKER_INTERACTIVE_C99 = $(DOCKER_BASE) \
	--hostname {{cookiecutter.project_slug}}_c99 \
	--interactive \
	--tty \
	--entrypoint bash \
	cookiecutter_c99

DOCKER_INTERACTIVE_PY36 = $(DOCKER_BASE) \
	--hostname {{cookiecutter.project_slug}}_py36 \
	--interactive \
	--tty \
	--entrypoint bash \
	cookiecutter_py36

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

.docker/cookiecutter_c99: Dockerfile.c99
	docker build --tag cookiecutter_c99 --file Dockerfile.c99 .
	mkdir -p .docker
	touch .docker/cookiecutter_c99

.docker/cookiecutter_py36: Dockerfile.py36
	docker build --tag cookiecutter_py36 --file Dockerfile.py36 .
	mkdir -p .docker
	touch .docker/cookiecutter_py36

.pre-commit:
	curl https://pre-commit.com/install-local.py | python -
	$(HOME)/bin/pre-commit install
	touch .pre-commit

.build: $(BUILD_DIR)
	touch .build

.conan: .docker/cookiecutter_c99 .build conanfile.txt
	$(DOCKER_RUN_C99) sh -c "mkdir -p $(BUILD_DIR) && cd $(BUILD_DIR) && conan install .."
	touch .conan

help:
	@echo "Welcome to {{cookiecutter.project}}!"
	@echo ""
	@echo "This project is managed with Docker. Please have Docker installed."
	@echo ""
	@echo "    uninstall-docker"
	@echo "        Remove Docker images cookiecutter_c99 and cookiecutter_py36"
	@echo "    init"
	@echo "        Initialize project directory"
	@echo "    docker-c99"
	@echo "        Start an interactive, Dockerized bash session using cookiecutter_c99"
	@echo "    docker-py36"
	@echo "        Start an interactive, Dockerized bash session using cookiecutter_py36"
	@echo "    pre-commit"
	@echo "        Execute pre-commit hooks"
	@echo "        See https://pre-commit.com/ for more information"
	@echo "    clean"
	@echo "        Clean the C99 project"
	@echo "    compile"
	@echo "        Compile the C99 project"
	@echo "    format"
	@echo "        Format the C99 project's code"
	@echo "        See https://clang.llvm.org/docs/ClangFormat.html for more information"
	@echo "    lint"
	@echo "        Lint the C99 project's code"
	@echo "        See http://oclint.org/ for more information"
	@echo "        Requires `make compile` to be executed prior to lint"
	@echo "    static-analysis"
	@echo "        Analyze the C99 project's code"
	@echo "        See https://clang-analyzer.llvm.org/scan-build.html for more information"
	@echo "        Requires `make compile` to be executed prior to analysis"
	@echo "    test"
	@echo "        Test the C99 project's code"
	@echo "        See https://docs.pytest.org/en/latest/ and https://cffi.readthedocs.io/en/latest/ for more information"

uninstall-docker:
	rm -rf .docker
	docker rmi --force cookiecutter_c99
	docker rmi --force cookiecutter_py36

init: .pre-commit

docker-c99: .docker/cookiecutter_c99
	$(DOCKER_INTERACTIVE_C99)

docker-py36: .docker/cookiecutter_py36
	$(DOCKER_INTERACTIVE_PY36)

pre-commit: .docker/cookiecutter_c99
	$(HOME)/bin/pre-commit run --all-files

clean:
	rm -f .build
	rm -f .conan
	rm -rf $(BUILD_DIR)
	rm -rf .hypothesis
	rm -rf .pytest_cache
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

compile: .docker/cookiecutter_c99 .build .conan
	$(DOCKER_RUN_C99) sh -c "cd $(BUILD_DIR) && cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .. && make"

format: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "find ./src -type f -name '*.[c|h]' | xargs clang-format -i -style=file -verbose"

lint: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "find ./src -type f -name '*.[c|h]' | xargs oclint -p=$(BUILD_DIR)"

static-analysis: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "cd $(BUILD_DIR) && scan-build make"

test: .docker/cookiecutter_py36
	$(DOCKER_RUN_PY36) sh -c "pytest --strict"

hook-format: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "git ls-files -- '*.c' '*.h' | xargs clang-format -i -style=file -verbose"

hook-lint: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "test -d $(BUILD_DIR) && git ls-files -- '*.c' '*.h' | xargs oclint -p=$(BUILD_DIR)" | grep -E "FilesWithViolations=0 P1=0 P2=0 P3=0"

hook-static-analysis: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "test -d $(BUILD_DIR) && cd $(BUILD_DIR) && scan-build make" | grep -E "scan-build: No bugs found."

.PHONY: help uninstall-docker init docker-c99 docker-py36 pre-commit clean compile format lint static-analysis test hook-format hook-lint hook-static-analysis
