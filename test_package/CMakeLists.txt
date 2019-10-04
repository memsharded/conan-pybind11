cmake_minimum_required(VERSION 3.2)
project(example)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_DEBUG ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})

# Using the pybind cmake helpers:
set(PYBIND11_PYTHON_VERSION 3.7)
find_package(pybind11 REQUIRED)
pybind11_add_module(example MODULE example.cpp)

# USING plain cmake:
# find_package(PythonLibs 3.7 REQUIRED)
# add_library(example SHARED "example.cpp")
# target_include_directories(example PRIVATE ${PYTHON_INCLUDE_DIRS})
# target_link_libraries(example PUBLIC ${PYTHON_LIBRARY})
# SET_TARGET_PROPERTIES(example PROPERTIES PREFIX "")
# if(WIN32)
#   set_target_properties(example PROPERTIES SUFFIX ".pyd")
# elseif(APPLE)
#   set_target_properties(example PROPERTIES SUFFIX ".so")
#   set_target_properties(example PROPERTIES MACOSX_RPATH ".")
#   set_target_properties(example PROPERTIES LINK_FLAGS "-undefined dynamic_lookup ")
# endif()