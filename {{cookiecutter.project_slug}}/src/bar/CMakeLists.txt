#
# Library
#

set(target bar)

#
# Sources
#

set(srcs_path ${CMAKE_CURRENT_SOURCE_DIR}/src)

set(hdrs_path ${CMAKE_CURRENT_SOURCE_DIR}/include/${target})

set(srcs
        ${srcs_path}/bar.c
)

set(hdrs
        ${hdrs_path}/bar.h
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
