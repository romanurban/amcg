import glfw
import math
from OpenGL.GL import *
from OpenGL.GLU import *


def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if not glfw.init():
    raise Exception("Failed to initialize GLFW")

window = glfw.create_window(800, 600, "Lab3", None, None)
if not window:
    glfw.terminate()
    raise Exception("Failed to create GLFW window")

glfw.set_window_pos(window, 100, 150)

glfw.make_context_current(window)

glfw.set_window_size_callback(window, window_resize)

window_resize(window, 800, 600)

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
    (200, 320),
    # (200, 340),
    (240, 320),
    # (240, 340),
    (240, 80),
    (260, 60),
    (320, 60),
    (340, 80),
    (340, 320),
    # (340, 340),
    (380, 320),
    # (380, 340),
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

R_points = [
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
]

R_moves = [
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
]

U_points = [
    # U letter
    (240, 20),
    (200, 60),
    (200, 320),
    # (200, 340),
    (240, 320),
    # (240, 340),
    (240, 80),
    (260, 60),
    (320, 60),
    (340, 80),
    (340, 320),
    # (340, 340),
    (380, 320),
    # (380, 340),
    (380, 60),
    (340, 20),
]

U_moves = [
    # U letter
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
]

O_points = [
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

O_moves = [
    # O letter outer shape
    -1,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    1,
    # O letter inner shape
    -1,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    9,
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

skip_codes = [
    5,
    6,
    7,
    15,
    16,
    17,
    19,
    20,
    22,
    24,
    25,
    26,
    28,
    30,
    31,
    32,
    34,
    35,
    36,
    38,
    40,
    42,
    43,
    44,
    46,
    47,
]

skip_codes_R = [
    5,
    6,
    7,
    15,
    16,
    17,
]

skip_codes_U = [1, 2, 4, 6, 7, 8, 10, 12]

skip_codes_O = [
    1,
    2,
    4,
    5,
    6,
    8,
    10,
    12,
    13,
    14,
    16,
    17,
]


def draw_shape(letter="all"):
    global move_codes, points, skip_codes
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glColor3f(0.2235, 1.0, 0.0784)  # 39FF14

    # Initialize the current point
    current_point = None

    if letter == "R":
        move_codes = R_moves
        points = R_points
        skip_codes = skip_codes_R
    elif letter == "U":
        move_codes = U_moves
        points = U_points
        skip_codes = skip_codes_U
    elif letter == "O":
        move_codes = O_moves
        points = O_points
        skip_codes = skip_codes_O

    # Loop through move codes and process accordingly
    for i, code in enumerate(move_codes):
        if code == -1:
            # Move without drawing
            current_point = None
        else:
            x, y = points[code - 1]  # Adjust for 0-based indexing
            x = int(x)
            y = int(y)

            x, y = apply_transformations(x, y, letter)

            if current_point is not None:
                if code in skip_codes:
                    # Draw the line in the background color to hide it
                    glColor3f(0, 0, 0)  # Black color
                else:
                    # Set the color for visible lines
                    glColor3f(0.2235, 1.0, 0.0784)  # 39FF14 (Green)

                # Draw a line from the current point to the new point
                glVertex2f(*current_point)
                glVertex2f(x, y)
            current_point = (x, y)

    glEnd()


def calculate_bezier_point(t, P0, P1, P2, P3):
    """Calculate a point on a Bezier curve with given control points and parameter t"""
    u = 1 - t
    tt = t * t
    uu = u * u
    uuu = uu * u
    ttt = tt * t

    point = (uuu * P0[0], uuu * P0[1])  # First term
    point = (
        point[0] + 3 * uu * t * P1[0],
        point[1] + 3 * uu * t * P1[1],
    )  # Second term
    point = (point[0] + 3 * u * tt * P2[0], point[1] + 3 * u * tt * P2[1])  # Third term
    point = (point[0] + ttt * P3[0], point[1] + ttt * P3[1])  # Fourth term

    return point


def draw_bezier_curve(P0, P1, P2, P3, letter):
    """Draw a cubic Bezier curve based on four control points"""
    glColor3f(0.2235, 1.0, 0.0784)  # 39FF14
    glBegin(GL_LINE_STRIP)
    for t in range(0, 101):
        point = calculate_bezier_point(t / 100, P0, P1, P2, P3)
        # glVertex2f(*point)
        glVertex2f(*apply_transformations(point[0], point[1], letter))
    glEnd()


def cleanup_artifact():
    # cleanup
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)

    glVertex2f(*apply_transformations(540, 60, "O"))
    glVertex2f(*apply_transformations(480, 60, "O"))
    glEnd()


R_curve_control_points = [(140, 320), (170, 300), (170, 220), (140, 200)]
R_inner_curve_control_points = [(80, 300), (140, 280), (140, 240), (80, 220)]

U_up_left = [(200, 320), (210, 345), (230, 345), (240, 320)]
U_up_right = [(340, 320), (350, 345), (370, 345), (380, 320)]
U_outer_bottom = [(200, 60), (250, 10), (330, 10), (380, 60)]
U_inner_bottom = [(240, 80), (265, 50), (310, 50), (340, 80)]

O_outer_bottom = [(420, 60), (480, 10), (540, 10), (600, 60)]
O_inner_bottom = [(460, 80), (500, 50), (520, 50), (560, 80)]
O_outer_up = [(420, 300), (480, 355), (540, 355), (600, 300)]
O_inner_up = [(460, 280), (500, 310), (520, 310), (560, 280)]

horizontal_shift = 0
vertical_shift = 0
scale_factor = 1
rotation_angle = 0
rotation_angle_R = 0
rotation_angle_U = 0
rotation_angle_O = 0


def apply_transformations(x, y, letter="all"):
    global horizontal_shift, vertical_shift, scale_factor, rotation_angle, rotation_angle_R, rotation_angle_U, rotation_angle_O

    # Scale
    x, y = x * scale_factor, y * scale_factor
    # Rotate
    if letter == "R":
        radians = math.radians(rotation_angle_R)
    elif letter == "U":
        radians = math.radians(rotation_angle_U)
    elif letter == "O":
        radians = math.radians(rotation_angle_O)
    else:
        radians = math.radians(rotation_angle)
    x_rotated = x * math.cos(radians) - y * math.sin(radians)
    y_rotated = x * math.sin(radians) + y * math.cos(radians)
    # Shift
    x_shifted, y_shifted = x_rotated + horizontal_shift, y_rotated + vertical_shift
    return x_shifted, y_shifted


# Keyboard callback function
def key_callback(window, key, scancode, action, mods):
    global horizontal_shift, vertical_shift, scale_factor, rotation_angle, rotation_angle_R, rotation_angle_U, rotation_angle_O
    if action in [glfw.PRESS, glfw.REPEAT]:
        if key == glfw.KEY_SPACE:
            rotation_angle_R -= 5
            rotation_angle_U += 5
            rotation_angle_O -= 5
        elif key == glfw.KEY_RIGHT:
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
        elif key == glfw.KEY_PERIOD:
            rotation_angle -= 5  # rotate clockwise
        elif key == glfw.KEY_COMMA:
            rotation_angle += 5  # rotate counterclockwise


glfw.set_key_callback(window, key_callback)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    # draw_shape()
    draw_shape("R")
    draw_shape("U")
    draw_shape("O")

    cleanup_artifact()

    # smoothing
    draw_bezier_curve(*R_curve_control_points, "R")
    draw_bezier_curve(*R_inner_curve_control_points, "R")
    draw_bezier_curve(*U_outer_bottom, "U")
    draw_bezier_curve(*U_inner_bottom, "U")
    draw_bezier_curve(*U_up_left, "U")
    draw_bezier_curve(*U_up_right, "U")
    draw_bezier_curve(*O_outer_bottom, "O")
    draw_bezier_curve(*O_inner_bottom, "O")
    draw_bezier_curve(*O_outer_up, "O")
    draw_bezier_curve(*O_inner_up, "O")

    glfw.swap_buffers(window)

glfw.terminate()