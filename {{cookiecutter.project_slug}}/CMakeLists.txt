cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

#
# Project
#

project({{cookiecutter.project_slug}}
		VERSION {{cookiecutter.version}}
		LANGUAGES C)

set(CMAKE_C_STANDARD 99)

#
# Directory(s)
#

add_subdirectory(src)

#
# Dependency(s)
#

include(${CMAKE_CURRENT_SOURCE_DIR}/build/conan_paths.cmake)

find_package(PkgConfig REQUIRED)

# pkg_search_module(Baz REQUIRED IMPORTED_TARGET <MODULE>+)

#
# Install(s)
#

include(GNUInstallDirs)
