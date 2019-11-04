# {{cookiecutter.project}}

{{cookiecutter.description}}

## Build

1. This project is managed with [Docker](https://www.docker.com/).
2. Useful project commands are `make` targets.
3. Any of the `make` targets can be executed to initialize the Docker environment.
4. Use `make docker-c99` for an interactive, Dockerized bash session to execute compiled executables.

### Makefile

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

### Provided Tools

- **Compiler**: [gcc](https://gcc.gnu.org/)
- **Code Coverage**: [gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html) + [lcov](http://ltp.sourceforge.net/coverage/lcov.php)
- **Code Formatter**: [clang-format](https://clang.llvm.org/docs/ClangFormat.html)
- **Code Linter**: [oclint](http://oclint.org/)
- **Debugger**: [cgdb](https://cgdb.github.io/)
- **Documentation**: [doxygen](http://doxygen.nl)
- **Dynamic Analysis**: [valgrind](http://valgrind.org)
- **Package Configs**: [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/)
- **Package Manager**: [conan](https://conan.io/)
- **Project Management**: [cmake](https://cmake.org)
- **Profiler**: [gprof](https://sourceware.org/binutils/docs/gprof/)
- **Static Analysis**: [scan-build](https://clang-analyzer.llvm.org/scan-build.html)
- **Testing**: [ctest](https://github.com/bvdberg/ctest) + [pytest](https://docs.pytest.org/en/latest/) + [cffi](https://cffi.readthedocs.io/en/latest/)

## Contact

**Email**: [{{cookiecutter.author_email}}](mailto:{{cookiecutter.author_email}})

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [jparkie/cookiecutter-c99](https://github.com/jparkie/cookiecutter-c99) project template.
