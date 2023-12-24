import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

points = [
    # R letter
    (20, 20),
    # outer shape
    (20, 340),
    (100, 340),
    (140, 320),
    (160, 300),
    (160, 220),
    (140, 200),
    (100, 180),
    (160, 20),
    (120, 20),
    (60, 180),
    (60, 20),
    # inner shape
    (60, 300),
    (80, 300),
    (120, 280),
    (120, 240),
    (80, 220),
    (60, 220),
    # U letter
    (240, 20),
    (200, 60),
    (200, 340),
    (240, 340),
    (240, 80),
    (260, 60),
    (320, 60),
    (340, 80),
    (340, 340),
    (380, 340),
    (380, 60),
    (340, 20),
    # O letter outer shape
    (460, 20),
    (420, 60),
    (420, 300),
    (460, 340),
    (560, 340),
    (600, 300),
    (600, 60),
    (560, 20),
    # O letter inner shape
    (480, 60),
    (460, 80),
    (460, 280),
    (480, 300),
    (540, 300),
    (560, 280),
    (560, 80),
    (540, 60),
]

move_codes = [
    # R letter outer shape
    -1,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    1,
    # inner shape
    -1,
    13,
    14,
    15,
    16,
    17,
    18,
    13,
    # U letter
    -1,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    19,
    # O letter outer shape
    -1,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    31,
    # O letter inner shape
    -1,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    39,
]

def draw_shape():
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glColor3f(0.2235, 1.0, 0.0784)  # 39FF14

    current_point = None

    for code in move_codes:
        if code == -1:
            # move without drawing
            current_point = None
        else:
            x, y = points[code - 1]  # adjust for 0-based indexing
            x = int(x)
            y = int(y)

            if current_point is not None:
                glVertex2f(*current_point)
                glVertex2f(x, y)
            current_point = (x, y)

    glEnd()

def draw_shape_3d_rev1(depth=-10):
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glColor3f(0.2235, 1.0, 0.0784)  # Color

    current_point_front = None
    current_point_back = None

    # Draw and connect front and back faces only when the pen is down
    for code in move_codes:
        if code == -1:
            current_point_front = None
            current_point_back = None
        else:
            x, y = points[code - 1]
            if current_point_front is not None:
                # Draw front face line
                glVertex3f(*current_point_front)
                glVertex3f(x, y, 0)
                # Draw back face line
                glVertex3f(*current_point_back)
                glVertex3f(x, y, depth)
                # Connect the previous and current points front to back
                glVertex3f(*current_point_front)
                glVertex3f(*current_point_back)
                glVertex3f(x, y, 0)
                glVertex3f(x, y, depth)

            current_point_front = (x, y, 0)
            current_point_back = (x, y, depth)

    glEnd()

horizontal_shift = 0
vertical_shift = 0
scale_factor = 1
rotation_angle_x = 0
rotation_angle_y = 0
rotation_angle_z = 0


# Keyboard callback function
def key_callback(window, key, scancode, action, mods):
    global horizontal_shift, vertical_shift, scale_factor
    global rotation_angle_x, rotation_angle_y, rotation_angle_z
    if action in [glfw.PRESS, glfw.REPEAT]:
        if key == glfw.KEY_RIGHT:
            horizontal_shift += 10
        elif key == glfw.KEY_LEFT:
            horizontal_shift -= 10
        elif key == glfw.KEY_UP:
            vertical_shift += 10
        elif key == glfw.KEY_DOWN:
            vertical_shift -= 10
        elif key == glfw.KEY_KP_ADD or key == glfw.KEY_EQUAL:
            scale_factor += 0.1
        elif key == glfw.KEY_KP_SUBTRACT or key == glfw.KEY_MINUS:
            scale_factor = max(0.1, scale_factor - 0.1)
        elif key == glfw.KEY_X:
            rotation_angle_x -= 5
        elif key == glfw.KEY_Y:
            rotation_angle_y -= 5
        elif key == glfw.KEY_Z:
            rotation_angle_z -= 5

# Function to set up the view
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if not glfw.init():
    raise Exception("Failed to initialize GLFW")

window = glfw.create_window(800, 600, "Lab5", None, None)
if not window:
    glfw.terminate()
    raise Exception("Failed to create GLFW window")

glEnable(GL_DEPTH_TEST) 
glfw.set_window_pos(window, 100, 150)
glfw.make_context_current(window)
glfw.set_window_size_callback(window, window_resize)

window_resize(window, 800, 600)

glfw.set_key_callback(window, key_callback)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    
    # Set up the projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(80, 800/600, 0.1, 2500.0)
    
    # Set up the modelview matrix to rotate the cube
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #glTranslatef(0, 0, -1000)
    glTranslatef(horizontal_shift - 400, vertical_shift - 300, -1000)
    glScalef(scale_factor, scale_factor, scale_factor)
    glRotatef(rotation_angle_x, 1, 0, 0)  # Rotate around the OX axis
    glRotatef(rotation_angle_y, 0, 1, 0)  # Rotate around the OY axis
    glRotatef(rotation_angle_z, 0, 0, 1)  # Rotate around the OZ axis
    glRotatef(-30, 0, 1, 0)  # Rotate the cube 30 degrees around a vector (0, 1, 0)
    
    draw_shape_3d_rev1(-100)
    
    glfw.poll_events()
    glfw.swap_buffers(window)

glfw.terminate()