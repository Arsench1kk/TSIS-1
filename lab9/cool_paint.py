import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    points = []
    drawing_mode = 'line'

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_l:  # line mode
                    drawing_mode = 'line'
                elif event.key == pygame.K_c:  # circle mode
                    drawing_mode = 'circle'
                elif event.key == pygame.K_e:  #  eraser mode
                    drawing_mode = 'eraser'
                elif event.key == pygame.K_t:  #  rectangle mode
                    drawing_mode = 'rectangle'
                elif event.key == pygame.K_s:  # square mode
                    drawing_mode = 'square'
                elif event.key == pygame.K_q: #right triangle mode
                    drawing_mode = 'right_triangle'
                elif event.key == pygame.K_a:
                    drawing_mode = 'equilateral_triangle'
                elif event.key == pygame.K_m:
                    drawing_mode = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                    radius = min(200, radius + 1)
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]

        screen.fill((0, 0, 0))

        i = 0
        while i < len(points) - 1:
            if drawing_mode == 'line':
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            elif drawing_mode == 'circle':
                pygame.draw.circle(screen, getColor(mode, i), points[i], radius)
            elif drawing_mode == 'rectangle':
                pygame.draw.rect(screen, getColor(mode, i), pygame.Rect(points[i], (radius * 2, radius * 2)))
            elif drawing_mode == 'eraser':
                pygame.draw.circle(screen, (0, 0, 0), points[i], radius)
            elif drawing_mode == 'square':
                pygame.draw.rect(screen, getColor(mode, i), pygame.Rect(points[i], (radius * 2, radius * 2)))
            elif drawing_mode == 'right_triangle':
                drawRightTriangle(screen, points[i], radius, getColor(mode, i))
            elif drawing_mode == 'equilateral_triangle':
                drawEquilateralTriangle(screen, points[i], radius, getColor(mode, i))
            elif drawing_mode == 'rhombus':
                drawRhombus(screen, points[i], radius, getColor(mode, i))
            i += 1

        pygame.display.flip()
        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode):
    color = getColor(color_mode, index)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def getColor(color_mode, index):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        return (c1, c1, c2)
    elif color_mode == 'red':
        return (c2, c1, c1)
    elif color_mode == 'green':
        return (c1, c2, c1)
    return (c1, c1, c1)


def drawRightTriangle(screen, position, size, color):
    # Calculate vertices
    top = (position[0], position[1] - size)
    right = (position[0] + size, position[1])
    pygame.draw.polygon(screen, color, [position, top, right])


def drawEquilateralTriangle(screen, position, size, color):
    # Calculate vertices
    height = size * math.sqrt(3) / 2
    vertex1 = (position[0] - size / 2, position[1] + height / 2)
    vertex2 = (position[0] + size / 2, position[1] + height / 2)
    vertex3 = (position[0], position[1] - height / 2)
    pygame.draw.polygon(screen, color, [vertex1, vertex2, vertex3])


def drawRhombus(screen, position, size, color):
    # Calculate vertices
    top = (position[0], position[1] - size)
    bottom = (position[0], position[1] + size)
    left = (position[0] - size, position[1])
    right = (position[0] + size, position[1])
    pygame.draw.polygon(screen, color, [top, right, bottom, left])


main()