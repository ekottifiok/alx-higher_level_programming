cmake_minimum_required(VERSION 3.16)
project(alx_higher_level_programming)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(
    check_linked_list
    10-main.c
    10-check_cycle.c
    10-linked_lists.c
)