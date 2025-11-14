#include <GL/glut.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    glColor3f(1.0, 1.0, 1.0);  
    glBegin(GL_TRIANGLES);      
        glVertex2f(-0.5f, -0.5f);   
        glVertex2f( 0.5f, -0.5f);  
        glVertex2f( 0.0f,  0.5f);  
    glEnd();

    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutCreateWindow("OpenGL Triangle");

    glClearColor(0, 0, 0, 1);   // black background
    gluOrtho2D(-1, 1, -1, 1);   // set 2D projection

    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}