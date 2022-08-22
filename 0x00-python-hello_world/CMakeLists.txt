cmake_minimum_required(VERSION 3.16)
project(0x00-python-hello_world)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(
    check_linked_list
    10-main.c
    10-check_cycle.c
    10-linked_lists.c
)