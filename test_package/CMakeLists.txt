cmake_minimum_required(VERSION 3.10)
project(example)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(PythonLibs REQUIRED)
find_package(PythonInterp REQUIRED)

execute_process(
    COMMAND ${PYTHON_EXECUTABLE} -c "import sysconfig;import sys; sys.stdout.write(sysconfig.get_config_var('EXT_SUFFIX'))"
    OUTPUT_VARIABLE EXT_SUFFIX)

add_library(example SHARED "example.cpp")
target_include_directories(example PRIVATE ${PYTHON_INCLUDE_DIRS})
target_link_libraries(example PUBLIC CONAN_PKG::pybind11 ${PYTHON_LIBRARY})
set_target_properties(example PROPERTIES SUFFIX ${EXT_SUFFIX})