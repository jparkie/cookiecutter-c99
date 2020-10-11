#
# Sources
#

set(srcs_path ${CMAKE_CURRENT_SOURCE_DIR}/src)

#
# Build Executable
#

add_executable({{cookiecutter.lib_slug}}_test ${srcs_path}/{{cookiecutter.lib_slug}}_test.c)

#
# Include Directories
#

target_include_directories({{cookiecutter.lib_slug}}_test
        PRIVATE
        ${DEFAULT_INCLUDE_DIRECTORIES}
        ${PROJECT_SOURCE_DIR}/extern/ctest
        ${PROJECT_SOURCE_DIR}/{{cookiecutter.lib_slug}}/src
        ${PROJECT_SOURCE_DIR}/{{cookiecutter.lib_slug}}/include
)

#
# Links
#

target_link_libraries({{cookiecutter.lib_slug}}_test ${PROJECT_NAME}::{{cookiecutter.lib_slug}})

# Local: target_link_libraries(${target} <LOCAL>)
# Conan: target_link_libraries(${target} <CONAN>::<CONAN>)
# PlgConfig: target_link_libraries(${target} PkgConfig::<PREFIX>)

#
# Tests
#

add_test({{cookiecutter.lib_slug}}_test {{cookiecutter.lib_slug}}_test)
