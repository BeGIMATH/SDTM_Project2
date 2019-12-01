cmake_minimum_required (VERSION 3.10)
project (TP4)

set(CMAKE_CXX_FLAGS -g -Wall)
include_directories (${TP4_SOURCE_DIR}/lib)
set(SOURCE tp4.c)

add_subdirectory (examples)
add_subdirectory(lib)