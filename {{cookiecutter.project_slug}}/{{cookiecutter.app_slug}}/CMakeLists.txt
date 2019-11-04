#
# Executable
#

set(target {{cookiecutter.app_slug}})

#
# Sources
#

set(srcs_path ${CMAKE_CURRENT_SOURCE_DIR}/src)

set(srcs
        ${srcs_path}/{{cookiecutter.app_slug}}.c
)

#
# Build Executable
#

add_executable(${target} ${srcs})

#
# Include Directories
#

target_include_directories(${target}
        PRIVATE
        ${DEFAULT_INCLUDE_DIRECTORIES}
        ${PROJECT_BINARY_DIR}/src/include
)

#
# Links
#

target_link_libraries(${target} ${PROJECT_NAME}::{{cookiecutter.lib_slug}})

# Local: target_link_libraries(${target} <LOCAL>)
# Conan: target_link_libraries(${target} <CONAN>::<CONAN>)
# PlgConfig: target_link_libraries(${target} PkgConfig::<PREFIX>)
