cmake_minimum_required(VERSION 3.30)
project(test_package LANGUAGES CXX)

find_package(fastnoise-lite REQUIRED CONFIG)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE fastnoise-lite::fastnoise-lite)
