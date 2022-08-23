cmake_minimum_required(VERSION 3.16)
project(alx_higher_level_programming)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(
    insert
    13-main.c
    13-insert_number.c
    linked_lists.c
)