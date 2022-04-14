cmake_minimum_required(VERSION 3.19)

project(simconnect_package CXX)

add_library(simconnect_package
    include/simconnect_package_test.h
    src/simconnect_package_test.cpp
    src/main.cpp
)

target_link_libraries(simconnect_package 
    PUBLIC
    Ws2_32
    optimized ${CMAKE_CURRENT_SOURCE_DIR}/lib/SimConnect.lib
    debug ${CMAKE_CURRENT_SOURCE_DIR}/lib/SimConnectDebug.lib
)

target_include_directories(simconnect_package PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/include")

add_executable(simconnect_package_test src/main.cpp)

target_link_libraries(simconnect_package_test
    PUBLIC
        simconnect_package
)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

install(TARGETS simconnect_package)
