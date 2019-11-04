# cookiecutter-c99

Cookiecutter template for a C99 application.

## Requirements

### cookiecutter

Please follow instructions at https://cookiecutter.readthedocs.io/en/latest/installation.html.

#### pip

```
pip install cookiecutter
```

#### Homebrew (macOS)

```
brew install cookiecutter
```
#### Ubuntu

```
sudo apt-get install cookiecutter
```

## Installation

Please execute the following command to create a new C99 application.

```
cookiecutter git@github.com:jparkie/cookiecutter-c99.git
```

### Configurations

```
> cookiecutter git@github.com:jparkie/cookiecutter-c99.git
project [example]:
project_slug [example]:
app_slug [app]:
lib_slug [example]:
version [0.1.0]:
description [N/A]:
author_email [N/A]:
```

## Features

### Dockerfile + Makefile + Jenkinsfile

- A `Dockerfile.c99` with useful C99 toolchains is provided to build the project.
- A `Makefile` is provided to execute various project commands within a Docker container.
- A `Jenkinsfile` is provided with the following stages: Checkout, Clean, Compile and Unit Test.

#### Makefile

```
> make help
Welcome to {{cookiecutter.project}}!

This project is managed with Docker. Please have Docker installed.

    uninstall-docker
        Remove Docker images cookiecutter_c99
    init
        Initialize project directory
    docker-c99
        Start an interactive, Dockerized bash session using cookiecutter_c99
    pre-commit
        Execute pre-commit hooks
        See https://pre-commit.com/ for more information
    clean
        Clean the C99 project
    compile
        Compile the C99 project
    compile-cffi
        Compile the C99 project's Python CFFI
    format
        Format the C99 project's code
        See https://clang.llvm.org/docs/ClangFormat.html for more information
    lint
        Lint the C99 project's code
        See http://oclint.org/ for more information
        Requires 'make compile' to be executed prior to lint
    static-analysis
        Analyze the C99 project's code
        See https://clang-analyzer.llvm.org/scan-build.html for more information
        Requires 'make compile' to be executed prior to static-analysis
    run
        Run executable
        Requires 'make compile' to be executed prior to run
    test-unit
        Run unit tests for the C99 project's code
        See https://github.com/bvdberg/ctest for more information
        Requires 'make compile' to be executed prior to test-unit
    test-functional
        Run functional tests for the C99 project's code
        See https://docs.pytest.org/en/latest/ and https://cffi.readthedocs.io/en/latest/ for more information
        Requires 'make compile' to be executed prior to test-functional
```

### Project Structure

```
> tree -a ./
./
├── .clang-format
├── .gitignore
├── .pre-commit-config.yaml
├── CMakeLists.txt
├── Dockerfile.c99
├── Jenkinsfile
├── Makefile
├── README.md
├── cmake
│   └── .gitkeep
├── conanfile.txt
├── extern
│   ├── .gitkeep
│   └── ctest
│       ├── .git
│       ├── .gitignore
│       ├── LICENSE
│       ├── Makefile
│       ├── README.md
│       ├── ctest.h
│       ├── ctest_output.png
│       ├── main.c
│       └── mytests.c
├── tests
│   ├── .gitkeep
│   ├── CMakeLists.txt
│   ├── functional
│   │   ├── __init__.py
│   │   └── {{cookiecutter.lib_slug}}_cffi
│   │       ├── __init__.py
│   │       └── compile_cffi.py
│   └── unit
│       ├── CMakeLists.txt
│       └── src
│           └── {{cookiecutter.lib_slug}}_test.c
├── {{cookiecutter.app_slug}}
│   ├── CMakeLists.txt
│   └── src
│       └── {{cookiecutter.app_slug}}.c
└── {{cookiecutter.lib_slug}}
    ├── CMakeLists.txt
    ├── include
    │   └── {{cookiecutter.lib_slug}}
    │       └── {{cookiecutter.lib_slug}}.h
    └── src
        └── {{cookiecutter.lib_slug}}.c

14 directories, 32 files
```
