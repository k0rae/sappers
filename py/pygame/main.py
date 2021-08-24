import pygame as pg
import sys
import random

WINDOW_HEIGHT = 401
WINDOW_WIDTH = 800

CELL_SIZE = 40
MINES_MAX = 10

FPS = 60

mines_count = 0
field = 0
window = 0
mines_found = 0

gameIsOver = False

def draw_cell(x, y):
    font = pg.font.SysFont("Comic Sans MS", 30)
    color = (200, 200, 200)
    fill = 1
    cell = field[x][y]
    rect = pg.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    if cell > 8:
        fill = 0
    elif cell < -1 and cell != -10:
        text = font.render(str(cell+10), False, (200, 200, 200))
        window.blit(text, (x*CELL_SIZE + CELL_SIZE//2, y*CELL_SIZE + CELL_SIZE // 2))
    elif cell == -10:
        fill = 0
        color = (0, 0, 200)
    pg.draw.rect(window, color, rect, fill)

def draw_grid():
    for x in range(10):
        for y in range(10):
            draw_cell(x, y)

def get_cell_from_coords(x, y):
    cx, cy = x // CELL_SIZE, y // CELL_SIZE
    if cx >= 10 or cx < 0 or cy >= 10 or cy < 0:
        return None
    return cx, cy

def init_field():
    global field
    field = []
    for x in range(10):
        field.append([])
        for y in range(10):
            field[x].append(0)

def game_over():
    print('game over.')
    # todo

def open_cells(x, y):
    if x > 9 or x < 0 or y > 9 or y < 0:
        return
    cell = field[x][y]
    if cell > -1 and cell < 9:
        field[x][y] = cell - 10
    if cell == 0:
        open_cells(x-1, y)
        open_cells(x-1, y-1)
        open_cells(x-1, y+1)
        open_cells(x, y-1)
        open_cells(x, y+1)
        open_cells(x+1, y-1)
        open_cells(x+1, y)
        open_cells(x+1, y+1)

def win():
    print('you won!')
    gameIsOver = True

def handle_click(x, y, button):
    global mines_found, gameIsOver
    if gameIsOver:
        return
    if not get_cell_from_coords(x, y):
        return
    cx, cy = get_cell_from_coords(x, y)
    cell = field[cx][cy]
    if button == 1:                           # left click
        if cell == -1:
            game_over()
        if cell > -1 and cell < 9:
            open_cells(cx, cy)

    elif button == 3:                         # right click
        if cell > 8:
            if cell == 9:
                mines_found -= 1
            field[cx][cy] = cell - 10
        else:
            if cell == -1:
                mines_found += 1
            field[cx][cy] += 10
    if mines_found == mines_count:
        win()

def create_mines():
    global mines_count
    while mines_count < MINES_MAX:
        mx = random.randint(0, 9)
        my = random.randint(0, 9)
        if field[mx][my] != -1:
            field[mx][my] = -1
            mines_count += 1

def get_mine(x, y):
    if x < 0 or x > 9 or y < 0 or y > 9:
        return 0
    if field[x][y] == -1:
        return 1
    else:
        return 0

def place_nums():
    global field
    for x in range(10):
        for y in range(10):
            if field[x][y] == -1:
                continue
            around = get_mine(x-1, y) + get_mine(x-1, y-1) + get_mine(x-1, y+1) + get_mine(x, y+1) + get_mine(x, y-1) + get_mine(x+1, y-1) + get_mine(x+1, y) + get_mine(x+1, y+1)
            field[x][y] = around

def fill_field():
    create_mines()
    place_nums()

def draw():
    global window
    window.fill((0, 0, 0))
    draw_grid()
    pg.display.flip()

def main():
    global field, mines_count, window
    clock = pg.time.Clock()

    window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption(">sapper")
    pg.font.init()

    mines_count = 0
    field = []

    init_field()
    fill_field()

    while True:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP:
                x, y = pg.mouse.get_pos()
                handle_click(x, y, event.button)
        draw()
        
        
        


if __name__ == '__main__':
    main()
