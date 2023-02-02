cmake_minimum_required(VERSION 3.15)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
#set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${PROJECT_SOURCE_DIR}/cmake/modules")

project(MainProjectName
        VERSION 1.0.0
        LANGUAGES CXX)

set(CONAN_INSTALL_COMMAND conan install ../conanfile.txt --build=missing --settings compiler.libcxx=libstdc++11)
if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
else()
    execute_process(COMMAND ${CONAN_INSTALL_COMMAND}
            WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    ) # add_custom_target
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
endif()

add_custom_target(ConanPackageInstall
        COMMAND ${CONAN_INSTALL_COMMAND}
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
) # add_custom_target

add_subdirectory(target)
