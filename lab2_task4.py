import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


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

window = glfw.create_window(800, 600, "Lab2 Task4", None, None)
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


def draw_shape():
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glColor3f(0.2235, 1.0, 0.0784)  # 39FF14

    # Initialize the current point
    current_point = None

    # Loop through move codes and process accordingly
    for i, code in enumerate(move_codes):
        if code == -1:
            # Move without drawing
            current_point = None
        else:
            x, y = points[code - 1]  # Adjust for 0-based indexing
            x = int(x)
            y = int(y)

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


def draw_bezier_curve(P0, P1, P2, P3):
    """Draw a cubic Bezier curve based on four control points"""
    glColor3f(0.2235, 1.0, 0.0784)  # 39FF14
    glBegin(GL_LINE_STRIP)
    for t in range(0, 101):
        point = calculate_bezier_point(t / 100, P0, P1, P2, P3)
        glVertex2f(*point)
    glEnd()


def cleanup_artifact():
    # cleanup
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex2f(540, 60)
    glVertex2f(480, 60)
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

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    draw_shape()

    cleanup_artifact()

    # smoothing
    draw_bezier_curve(*R_curve_control_points)
    draw_bezier_curve(*R_inner_curve_control_points)
    draw_bezier_curve(*U_outer_bottom)
    draw_bezier_curve(*U_inner_bottom)
    draw_bezier_curve(*U_up_left)
    draw_bezier_curve(*U_up_right)
    draw_bezier_curve(*O_outer_bottom)
    draw_bezier_curve(*O_inner_bottom)
    draw_bezier_curve(*O_outer_up)
    draw_bezier_curve(*O_inner_up)

    glfw.swap_buffers(window)

glfw.terminate()