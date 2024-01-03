import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Function to set up the view
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # gluOrtho2D(0, width, 0, height)
    # gluOrtho2D(0, width*4, 0, height) # narrow horizontally
    # gluOrtho2D(0, width, 0, height*4) # narrow vertically
    gluOrtho2D(0, width, height, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Initialize GLFW
if not glfw.init():
    raise Exception("Failed to initialize GLFW")

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(400, 300, "Lab1 Task2", None, None)
if not window:
    glfw.terminate()
    raise Exception("Failed to create GLFW window")

# Set the window position
glfw.set_window_pos(window, 100, 150)

# Make the window's context current
glfw.make_context_current(window)

# Set the window resize callback
glfw.set_window_size_callback(window, window_resize)

# Set up the view
window_resize(window, 400, 300)

# Points and move codes
points = [(50, 35), (50, 55), (40, 45), (60, 45), (50, 55)]
move_codes = [0, 1, 1, 1, 1]

# Points and move codes for optimized version
opt_points = [(50, 35), (50, 55), (40, 45), (60, 45)]
opt_move_codes = [-1, 1, 2, 3, 4, 2]

xshift = 35 
yshift = 15
scaling_factor = 3.5

def draw_shape():
    glLineWidth(2.0)

    glBegin(GL_LINES)
    glColor3f(0.2235, 1.0, 0.0784) #39FF14

    current_point = None
    for i, code in enumerate(move_codes):
        x, y = points[i]
        # apply the scaling factor to the coordinates and cast to integers
        x = int(x * scaling_factor + xshift)
        y = int(y * scaling_factor + yshift)
        if code == 0:
            current_point = (x, y)
        elif code == 1 and current_point is not None:
            glVertex2f(*current_point)
            glVertex2f(x, y)
            current_point = (x, y)
    glEnd()

def draw_shape_opt():
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(0.2235, 1.0, 0.0784)  # 39FF14
    
    current_point = None
    
    for code in opt_move_codes:
        if code == -1:
            # Move without drawing
            current_point = None
        else:
            x, y = opt_points[code - 1]  # Adjust for 0-based indexing
            # Apply the scaling factor to the coordinates
            x = int(x * scaling_factor + xshift)
            y = int(y * scaling_factor + yshift)
            
            if current_point is not None:
                glVertex2f(*current_point)
                glVertex2f(x, y)
            current_point = (x, y)
    
    glEnd()


while not glfw.window_should_close(window):
    glfw.poll_events()

    # Clear the screen
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    # draw_shape()
    draw_shape_opt()

    glfw.swap_buffers(window)

glfw.terminate()