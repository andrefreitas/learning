cmake_minimum_required(VERSION 3.2)
project(OpenGL)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)

find_package(OpenGL REQUIRED)
find_package(GLEW REQUIRED)
find_package(GLM REQUIRED)
find_package(SDL2 REQUIRED)

include_directories(/usr/local/include ${OPENGL_INCLUDE_DIRS} ${GLEW_INCLUDE_DIRS} ${GLM_INCLUDE_DIRS} ${SDL2_INCLUDE_DIR})

set(SOURCE_FILES main.cpp)
add_executable(OpenGL ${SOURCE_FILES} Display.cpp Display.h Shader.cpp Shader.h Mesh.cpp Mesh.h)
target_link_libraries(OpenGL ${OPENGL_LIBRARIES} ${GLEW_LIBRARIES} ${SDL2_LIBRARY})