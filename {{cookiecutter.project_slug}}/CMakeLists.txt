cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

#
# Project
#

project({{cookiecutter.project_slug}}
		VERSION {{cookiecutter.version}}
		LANGUAGES C)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
set(CMAKE_C_STANDARD 99)

#
# Test(s)
#
include(CTest)

#
# Directory(s)
#

add_subdirectory({{cookiecutter.app_slug}})
add_subdirectory({{cookiecutter.lib_slug}})
add_subdirectory(tests)

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
