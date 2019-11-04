#
# Library
#

set(target {{cookiecutter.lib_slug}})

#
# Coverage
#

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
        set(CMAKE_C_FLAGS ${CMAKE_C_FLAGS} "-g -O0 -fprofile-arcs -ftest-coverage")
        set(CMAKE_C_OUTPUT_EXTENSION_REPLACE ON)
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} --coverage")
endif()

#
# Sources
#

set(srcs_path ${CMAKE_CURRENT_SOURCE_DIR}/src)

set(hdrs_path ${CMAKE_CURRENT_SOURCE_DIR}/include/${target})

set(srcs
        ${srcs_path}/{{cookiecutter.lib_slug}}.c
)

set(hdrs
        ${hdrs_path}/{{cookiecutter.lib_slug}}.h
)

#
# Build Library
#

add_library(${target} SHARED ${srcs} ${hdrs})

#
# Create Namespaced Alias
#

add_library(${PROJECT_NAME}::${target} ALIAS ${target})

#
# Export Library
#

export(TARGETS ${target} NAMESPACE ${PROJECT_NAME}:: FILE ${PROJECT_BINARY_DIR}/cmake/${target}/${target}-export.cmake)

#
# Include Directories
#

target_include_directories(${target}
        PRIVATE
        ${PROJECT_BINARY_DIR}/src/include
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        ${CMAKE_CURRENT_BINARY_DIR}/include
        PUBLIC
        ${DEFAULT_INCLUDE_DIRECTORIES}
        INTERFACE
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/include>
        $<INSTALL_INTERFACE:include>
)

#
# Links
#

# Local: target_link_libraries(${target} <LOCAL>)
# Conan: target_link_libraries(${target} <CONAN>::<CONAN>)
# PkConfig: target_link_libraries(${target} PkgConfig::<PREFIX>)
