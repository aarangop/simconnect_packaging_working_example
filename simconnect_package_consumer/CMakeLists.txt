cmake_minimum_required(VERSION 3.15)
project(simconnect_consumer CXX)

set(CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH} ${CMAKE_BINARY_DIR})

find_package(simconnect_package CONFIG REQUIRED)

add_executable(simconnect_consumer 
    src/simconnect_consumer.cpp 
    src/main.cpp
)

if (TARGET simconnect_package::simconnect_package)
    target_link_libraries(simconnect_consumer simconnect_package::simconnect_package)
endif()

target_include_directories(simconnect_consumer PUBLIC include)

install(TARGETS simconnect_consumer)
