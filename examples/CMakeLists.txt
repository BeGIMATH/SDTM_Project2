
link_directories (${TP4_BINARY_DIR}/lib)
add_executable(test1 test1.c)
target_link_libraries(test1 tp4)

add_executable(test2 test2.c)
target_link_libraries(test2 tp4)

