#ifndef SHADER_H
#define SHADER_H

#include <string>
#include <GL/glew.h>

class Shader {
public:
    Shader(const std::string& fileName);
    void Bind();
    virtual ~Shader();
    static std::string LoadShader(const std::string& fileName);
    static void CheckShaderError(GLuint shader, GLuint flag, bool isProgram, const std::string& errorMessage);
    static GLuint CreateShader(const std::string &text, GLenum shaderType);
protected:
private:
    static const unsigned int NUM_SHADERS = 2;
    Shader(const Shader& other){}
    void operator=(const Shader& other){}

    GLuint m_program;
    GLuint m_shaders[NUM_SHADERS];
};


#endif //SHADER_H
