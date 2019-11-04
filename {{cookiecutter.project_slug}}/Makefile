BUILD_DIR = build

DOCKER_BASE = docker run \
	--volume $$(pwd):/repo \
	--volume /var/run/docker.sock:/var/run/docker.sock \
	--volume $(HOME)/.conan:/root/.conan \
	--net host \
	--tty

DOCKER_RUN_C99 = $(DOCKER_BASE) \
	cookiecutter_c99

DOCKER_INTERACTIVE_C99 = $(DOCKER_BASE) \
	--hostname {{cookiecutter.project_slug}}_c99 \
	--interactive \
	--tty \
	--entrypoint bash \
	cookiecutter_c99

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

.docker/cookiecutter_c99: Dockerfile.c99
	docker build --rm --tag cookiecutter_c99 --file Dockerfile.c99 .
	mkdir -p .docker
	touch .docker/cookiecutter_c99

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
	@echo "        Remove Docker images cookiecutter_c99"
	@echo "    init"
	@echo "        Initialize project directory"
	@echo "    docker-c99"
	@echo "        Start an interactive, Dockerized bash session using cookiecutter_c99"
	@echo "    pre-commit"
	@echo "        Execute pre-commit hooks"
	@echo "        See https://pre-commit.com/ for more information"
	@echo "    clean"
	@echo "        Clean the C99 project"
	@echo "    compile"
	@echo "        Compile the C99 project"
	@echo "    compile-cffi"
	@echo "        Compile the C99 project's Python CFFI"
	@echo "    format"
	@echo "        Format the C99 project's code"
	@echo "        See https://clang.llvm.org/docs/ClangFormat.html for more information"
	@echo "    lint"
	@echo "        Lint the C99 project's code"
	@echo "        See http://oclint.org/ for more information"
	@echo "        Requires 'make compile' to be executed prior to lint"
	@echo "    static-analysis"
	@echo "        Analyze the C99 project's code"
	@echo "        See https://clang-analyzer.llvm.org/scan-build.html for more information"
	@echo "        Requires 'make compile' to be executed prior to static-analysis"
	@echo "    run"
	@echo "        Run executable"
	@echo "        Requires 'make compile' to be executed prior to run"
	@echo "    test-unit"
	@echo "        Run unit tests for the C99 project's code"
	@echo "        See https://github.com/bvdberg/ctest for more information"
	@echo "        Requires 'make compile' to be executed prior to test-unit"
	@echo "    test-functional"
	@echo "        Run functional tests for the C99 project's code"
	@echo "        See https://docs.pytest.org/en/latest/ and https://cffi.readthedocs.io/en/latest/ for more information"
	@echo "        Requires 'make compile' to be executed prior to test-functional"

uninstall-docker:
	rm -rf .docker
	docker rmi --force cookiecutter_c99

init: .pre-commit
	cd extern && git submodule add https://github.com/bvdberg/ctest.git

docker-c99: .docker/cookiecutter_c99
	$(DOCKER_INTERACTIVE_C99)

pre-commit: .docker/cookiecutter_c99
	$(HOME)/bin/pre-commit run --all-files

clean:
	rm -f .build
	rm -f .conan
	rm -rf $(BUILD_DIR)
	rm -rf .hypothesis
	rm -rf .pytest_cache
	rm -rf ./tests/functional/{{cookiecutter.lib_slug}}_cffi/_{{cookiecutter.lib_slug}}_cffi.*
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

compile: .docker/cookiecutter_c99 .build .conan
	$(DOCKER_RUN_C99) sh -c "cd $(BUILD_DIR) && cmake -DCMAKE_BUILD_TYPE=Debug -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .. && make"

compile-cffi: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "cd tests/functional/{{cookiecutter.lib_slug}}_cffi \
		&& python3 -m compile_cffi \
			/repo/{{cookiecutter.lib_slug}}/include \
			/repo/$(BUILD_DIR)/{{cookiecutter.lib_slug}}"

format: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "find ./{{cookiecutter.app_slug}} ./{{cookiecutter.lib_slug}} -type f -name '*.[c|h]' | xargs clang-format -i -style=file -verbose"

lint: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "find ./{{cookiecutter.app_slug}} ./{{cookiecutter.lib_slug}} -type f -name '*.[c|h]' | xargs oclint -p=$(BUILD_DIR)"

static-analysis: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "cd $(BUILD_DIR) && scan-build make"

run: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "./$(BUILD_DIR)/{{cookiecutter.app_slug}}/{{cookiecutter.app_slug}}"

test-unit: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "cd $(BUILD_DIR) \
		&& lcov --directory ./{{cookiecutter.lib_slug}} --zerocounters \
		&& lcov --capture --initial --directory ./{{cookiecutter.lib_slug}} --output-file coverage_base.info \
		&& ctest --verbose \
		&& lcov --capture --directory ./{{cookiecutter.lib_slug}} --output-file coverage_test.info \
		&& lcov --add-tracefile coverage_base.info --add-tracefile coverage_test.info --output-file coverage_total.info \
		&& lcov --remove coverage_total.info '{{cookiecutter.app_slug}}/*' 'tests/unit/*' --output-file coverage_total_filtered.info \
		&& genhtml coverage_total_filtered.info --output-directory coverage"
	@echo "Coverage Report: $$(pwd)/$(BUILD_DIR)/coverage/index.html"

test-functional: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "cd tests/functional && pytest -rA --strict --hypothesis-show-statistics"

hook-format: .docker/cookiecutter_c99
	$(DOCKER_RUN_C99) sh -c "git ls-files -- './{{cookiecutter.app_slug}}/*.c' './{{cookiecutter.app_slug}}/*.h' './{{cookiecutter.lib_slug}}/*.c' './{{cookiecutter.lib_slug}}/*.h' | xargs clang-format -i -style=file -verbose"

hook-lint: .docker/cookiecutter_c99
	test -d $(BUILD_DIR) && $(DOCKER_RUN_C99) sh -c "git ls-files -- './{{cookiecutter.app_slug}}/*.c' './{{cookiecutter.app_slug}}/*.h' './{{cookiecutter.lib_slug}}/*.c' './{{cookiecutter.lib_slug}}/*.h' | xargs oclint -p=$(BUILD_DIR)" | grep -E "P1=0"

hook-static-analysis: .docker/cookiecutter_c99
	test -d $(BUILD_DIR) && $(DOCKER_RUN_C99) sh -c "cd $(BUILD_DIR) && scan-build make" | grep -E "scan-build: No bugs found."

.PHONY: help uninstall-docker init docker-c99 pre-commit clean compile compile-cffi format lint static-analysis run test-unit test-functional hook-format hook-lint hook-static-analysis
