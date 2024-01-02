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

def draw_quad_strip(points, depth, letter):
    glBegin(GL_QUAD_STRIP)
    glColor3f(0.45098, 0.57647, 0.70196)
    for x, y in points:
        glVertex3f(x, y, 0)  # Front vertex
        glVertex3f(x, y, depth)  # Corresponding back vertex
    # Close the quad strip by connecting the last vertices to the first
    if letter != "R":
        glVertex3f(points[0][0], points[0][1], 0)  # First front vertex
        glVertex3f(points[0][0], points[0][1], depth)  # First corresponding back vertex
    # special case for R
    else: 
        glVertex3f(points[11][0], points[11][1], 0)  # First front vertex
        glVertex3f(points[11][0], points[11][1], depth)  # First corresponding back vertex
        glVertex3f(points[0][0], points[0][1], 0)  # First front vertex
        glVertex3f(points[0][0], points[0][1], depth)  # First corresponding back vertex
    glEnd()

def draw_shape_3d_rev1(depth=-10):
    
    glColor3f(0.2235, 1.0, 0.0784)  # color for R letter
    draw_quads_for_face(r_quads, 0) # Front face
    draw_triangles_for_face(r_triangles[0][0], r_triangles[0][1], r_triangles[0][2], 0) # Front face
    draw_triangles_for_face(r_triangles[1][0], r_triangles[1][1], r_triangles[1][2], 0) # Front face
    draw_triangles_for_face(r_triangles[2][0], r_triangles[2][1], r_triangles[2][2], 0) # Front face
    draw_triangles_for_face(r_triangles[3][0], r_triangles[3][1], r_triangles[3][2], 0) # Front face
    draw_triangles_for_face(r_triangles[4][0], r_triangles[4][1], r_triangles[4][2], 0) # Front face
    
    glColor3f(0.0, 1.0, 1.0)
    draw_quads_for_face(r_quads, -50) # Back face
    draw_triangles_for_face(r_triangles[0][2], r_triangles[0][1], r_triangles[0][0], -50) # Back face
    draw_triangles_for_face(r_triangles[1][2], r_triangles[1][1], r_triangles[1][0], -50) # Back face
    draw_triangles_for_face(r_triangles[2][2], r_triangles[2][1], r_triangles[2][0], -50) # Back face
    draw_triangles_for_face(r_triangles[3][2], r_triangles[3][1], r_triangles[3][0], -50) # Back face
    draw_triangles_for_face(r_triangles[4][2], r_triangles[4][1], r_triangles[4][0], -50) # Back face
    draw_quad_strip(points[0:18], depth, "R")  # Draw R letter


    draw_quad_strip(points[18:30], depth, "U")  # Draw U letter
    glColor3f(0.862, 0.078, 0.235)
    draw_quads_for_face(u_quads, 0) # Front face
    draw_triangles_for_face(u_triangles[0][0], u_triangles[0][1], u_triangles[0][2], 0) # Front face
    draw_triangles_for_face(u_triangles[1][0], u_triangles[1][1], u_triangles[1][2], 0) # Front face
    glColor3f(1.0, 1.0, 0.0)
    draw_quads_for_face(u_quads, -50)  # Back face
    draw_triangles_for_face(u_triangles[0][2], u_triangles[0][1], u_triangles[0][0], -50) # Back face
    draw_triangles_for_face(u_triangles[1][2], u_triangles[1][1], u_triangles[1][0], -50) # Back face

    
    draw_quad_strip(points[30:38], depth, "O")  # Draw O letter outer shape
    draw_quad_strip(points[38:47], depth, "0")  # Draw O letter inner shape
    glColor3f(0.0, 0.0, 1.0)  # Blue color for O letter outer shape
    draw_quads_for_face(o_quads, 0) # Front face
    draw_triangles_for_face(o_triangles[0][0], o_triangles[0][1], o_triangles[0][2], 0) # Front face
    draw_triangles_for_face(o_triangles[1][0], o_triangles[1][1], o_triangles[1][2], 0) # Front face
    draw_triangles_for_face(o_triangles[2][0], o_triangles[2][1], o_triangles[2][2], 0) # Front face
    draw_triangles_for_face(o_triangles[3][0], o_triangles[3][1], o_triangles[3][2], 0) # Front face

    glColor3f(1.0, 0.0, 1.0)
    draw_quads_for_face(o_quads, -50) # Back face
    draw_triangles_for_face(o_triangles[0][2], o_triangles[0][1], o_triangles[0][0], -50) # Back face
    draw_triangles_for_face(o_triangles[1][2], o_triangles[1][1], o_triangles[1][0], -50) # Back face
    draw_triangles_for_face(o_triangles[2][2], o_triangles[2][1], o_triangles[2][0], -50) # Back face
    draw_triangles_for_face(o_triangles[3][2], o_triangles[3][1], o_triangles[3][0], -50) # Back face

def draw_polygon_face(face_points, depth):
    glBegin(GL_POLYGON)

    for x, y in face_points:
        glVertex3f(x, y, depth)

    glEnd()

def draw_quads_for_face(face_points, depth):
    glBegin(GL_QUADS)
    if depth >= 0:
        order = [0, 1, 2, 3]  # Normal counterclockwise order
    else:
        order = [3, 2, 1, 0]  # Reverse order for negative depth

    for i in range(0, len(face_points), 4):
        for j in order:  # Use the order list to draw vertices
            glVertex3f(face_points[i + j][0], face_points[i + j][1], depth)
    glEnd()

def draw_triangles_for_face(v1, v2, v3, depth):
    # Draw a single triangle at the given depth
    glBegin(GL_TRIANGLES)
    glVertex3f(v1[0], v1[1], depth)
    glVertex3f(v2[0], v2[1], depth)
    glVertex3f(v3[0], v3[1], depth)
    glEnd()

r_quads = [
    # Left vertical side
    (60, 20), (60, 340), (20, 340), (20, 20), 
    # R right diagonal
    (120, 20), (160, 20), (100, 180), (60, 180),
    # right vertical
    (120,190), (160,220), (160,300), (120,330),
    
	(100, 340), (20, 340), (20, 300), (100, 300), 
    (100, 220), (60, 220), (60, 180), (100, 180),
    (120, 240), (100, 220), (100, 180), (120, 190),
    (120, 320), (100, 340), (100, 300), (120, 280), 
]

r_triangles = [
    [(120, 280), (110, 300), (80, 300)],
    [(120,240), (80,220), (110,220)],
    [(160, 220), (100, 180), (140, 200)],
    [(160, 300), (140, 320), (100, 340)],
    [(140, 320), (100, 340), (100, 290)],
]

o_quads = [
    # Left vertical side
    (460, 20), (460, 340), (420, 300), (420, 60),
    # Right vertical side
    (600, 60), (600, 300), (560, 340), (560, 20),
    # Top horizontal
    (560, 300), (560, 340), (460, 340), (460, 300),
    # Bottom horizontal
    (560, 60), (460, 60), (460, 20), (560, 20),
 ]

o_triangles = [
    # Top Left
    [(460, 300), (460, 280), (480, 300)],
    # Top Right
    [(560,300),(540,300),(560,280)],
    # Bottom Left
    [(460, 60), (480, 60), (460, 80)],
    # Bottom Right
    [(560,60),(560,80),(540,60)],
]

u_quads = [
    # Left vertical side
    (200, 60), (240, 20), (240, 340), (200, 340),
    # Bottom quad
    (240,20),(340,20),(340,60),(240,60),
    # Right vertical side
    (340,340),(340,20),(380,60),(380,340),
]

u_triangles = [
    # left
    [(240,60),(260,60),(240,80)],
    # right
    [(320, 60), (340, 60), (340, 80)],
]

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

def setup_lighting():
    glEnable(GL_LIGHTING)  # Enable lighting
    glEnable(GL_LIGHT0)  # Enable light #0
    glEnable(GL_COLOR_MATERIAL)  # Enable color tracking
    glColorMaterial(GL_FRONT, GL_DIFFUSE)  # Set material to follow diffuse and ambient

    # Define ambient, diffuse, and specular components for light 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.1, 0.1, 0.1, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1])
    glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.02])  # Directional light
    
    # Adjust the global ambient light level
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1])
    
    # Enable depth testing for correct z-ordering
    glEnable(GL_DEPTH_TEST)

if not glfw.init():
    raise Exception("Failed to initialize GLFW")

window = glfw.create_window(800, 600, "Lab6", None, None)
if not window:
    glfw.terminate()
    raise Exception("Failed to create GLFW window")

glfw.set_window_pos(window, 100, 150)
glfw.make_context_current(window)
glfw.set_window_size_callback(window, window_resize)

window_resize(window, 800, 600)

glfw.set_key_callback(window, key_callback)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    # Set up the projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(80, 800/600, 0.1, 2500.0)
    
    # Set up the modelview matrix to rotate the cube
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #glTranslatef(0, 0, -500)
    glTranslatef(horizontal_shift - 400, vertical_shift - 300, -500)
    glScalef(scale_factor, scale_factor, scale_factor)
    glRotatef(rotation_angle_x, 1, 0, 0)  # Rotate around the OX axis
    glRotatef(rotation_angle_y, 0, 1, 0)  # Rotate around the OY axis
    glRotatef(rotation_angle_z, 0, 0, 1)  # Rotate around the OZ axis
    glRotatef(-30, 0, 1, 0)  # Rotate the cube 30 degrees around a vector (0, 1, 0)
    

    # Setup lighting
    setup_lighting()
    draw_shape_3d_rev1(-50)
    
    glfw.poll_events()
    glfw.swap_buffers(window)

glfw.terminate()