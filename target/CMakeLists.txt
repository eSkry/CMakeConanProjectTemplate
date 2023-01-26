set(PROJECT_NAME MyProject)

project(${PROJECT_NAME} VERSION 1.0.0 LANGUAGES CXX C)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_executable(${PROJECT_NAME} "main.cpp")

set_target_properties(${PROJECT_NAME} PROPERTIES
        VERSION ${PROJECT_VERSION}
        SOVERSION ${PROJECT_VERSION}
        OUTPUT_NAME ${PROJECT_NAME}
) # set_target_properties

target_include_directories(${PROJECT_NAME}
        PUBLIC ${CONAN_INCLUDE_DIRS}
) # target_include_directories

target_link_directories(${PROJECT_NAME}
        PUBLIC ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}
) # target_link_directories

target_link_libraries(${PROJECT_NAME}
        PUBLIC ${CONAN_LIBS}
) # target_link_libraries


target_compile_options(${PROJECT_NAME}
        PRIVATE $<$<CONFIG:Debug>:-O0>
        PRIVATE $<$<CONFIG:Release>:-O2>
        PUBLIC $<$<STREQUAL:${CMAKE_CXX_COMPILER_ID}, MSVC>:"/Zc:__cplusplus">
) # target_compile_options
