import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def abs_func(x):
    return abs(1/4 * x + 3 * math.cos(100 * x) * math.sin(x))

x_min, x_max, step = -100, 100, 0.5

y_max_value = max([abs_func(x) for x in range(int(x_min), int(x_max) + 1)])
y_min, y_max = -y_max_value, y_max_value + 5

def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(x_min, x_max, y_min, y_max)
    glMatrixMode(GL_MODELVIEW)

def draw_axis():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # draw OX and OY axes
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(2.0)
    glBegin(GL_LINES) # begin defining a series of line segments
    glVertex2f(x_min, 0)
    glVertex2f(x_max, 0)
    glVertex2f(0, y_min)
    glVertex2f(0, y_max)
    glEnd()

    # draw tick marks on the axes
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(4.0)
    glBegin(GL_LINES)
    for x_tick in range(int(x_min), int(x_max) + 1, 10):
        glVertex2f(x_tick, -0.5)
        glVertex2f(x_tick, 0.5)
    for y_tick in range(int(y_min), int(y_max) + 1, 2):
        glVertex2f(-0.5, y_tick)
        glVertex2f(0.5, y_tick)
    glEnd()


def draw_graph():
    glColor3f(0.2235, 1.0, 0.0784) #39FF14
    glLineWidth(2.0)
    glBegin(GL_LINES)
    x = x_min
    while x < x_max:
        y1 = abs_func(x)
        y2 = abs_func(x + step)
        glVertex2f(x, y1)
        glVertex2f(x + step, y2)
        x += step
    glEnd()


def add_glow_effect():
    # add glow effect by drawing lines slightly above and below
    # with color intensity gradient
    num_iterations = 6  # Number of intensity reduction iterations
    initial_intensity = 0.1  # Initial green intensity

    for i in range(num_iterations):
        intensity = initial_intensity + i * 0.1  # Increase intensity in each iteration
        glColor3f(0.0, intensity, 0.0)  # Set color with reduced intensity

        glBegin(GL_LINES)
        x = x_min
        while x < x_max:
            y1 = abs_func(x) + 0.1 * (num_iterations - i)  # Draw above the main line
            y2 = abs_func(x + step) + 0.1 * (num_iterations - i)
            glVertex2f(x, y1)
            glVertex2f(x + step, y2)
            x += step
        glEnd()

        glBegin(GL_LINES)
        x = x_min
        while x < x_max:
            y1 = abs_func(x) - 0.1 * (num_iterations - i)  # Draw below the main line
            y2 = abs_func(x + step) - 0.1 * (num_iterations - i)
            glVertex2f(x, y1)
            glVertex2f(x + step, y2)
            x += step
        glEnd()

if not glfw.init():
    raise Exception("Failed to initialize GLFW")

window = glfw.create_window(800, 600, "Lab1 Task1", None, None)
if not window:
    glfw.terminate()
    raise Exception("Failed to create GLFW window")

glfw.make_context_current(window)

glfw.set_window_size_callback(window, window_resize)

window_resize(window, 800, 600)

while not glfw.window_should_close(window):
    glfw.poll_events()
    draw_axis()
    add_glow_effect()
    draw_graph()
    glfw.swap_buffers(window)

glfw.terminate()