import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Function to draw the cube
def draw_cube():
    # Define the 8 vertices of the cube
    vertices = [
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, -1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, 1]
    ]

    # Define the 6 faces of the cube, each with 4 vertices, using the indices above
    faces = [
        [0, 1, 2, 3],
        [3, 2, 7, 6],
        [6, 7, 5, 4],
        [4, 5, 1, 0],
        [1, 5, 7, 2],
        [4, 0, 3, 6]
    ]

    # Start drawing the cube
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main function to set up the window and run the main loop
def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "3D Cube", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D

    # Main loop that will continue until the window is closed
    while not glfw.window_should_close(window):
        # Render here, e.g. clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Set up the projection matrix
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 640/480, 0.1, 50.0)

        # Set up the modelview matrix to rotate the cube
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -5)  # Move the cube so it's within view (5 units into the screen)
        glRotatef(30, 1, 1, 0)  # Rotate the cube 30 degrees around a vector (1, 1, 0)

        # Draw the cube
        draw_cube()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
