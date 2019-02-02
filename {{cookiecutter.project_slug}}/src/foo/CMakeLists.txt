#
# Executable
#

set(target foo)

#
# Sources
#

set(srcs_path ${CMAKE_CURRENT_SOURCE_DIR}/src)

set(srcs
        ${srcs_path}/foo.c
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

target_link_libraries(${target} ${PROJECT_NAME}::bar)

# Local: target_link_libraries(foo <LOCAL>)
# Conan: target_link_libraries(foo <CONAN>::<CONAN>)
# PlgConfig: target_link_libraries(foo PkgConfig::<PREFIX>)
