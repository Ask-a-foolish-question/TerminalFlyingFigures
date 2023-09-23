import os
import time
from colorama import Fore, Back

width, height = 80, 24
screen = [[' ' for _ in range(width)] for _ in range(height)]

elements = [
    {'x': 0, 'y': 0, 'vx': 1, 'vy': 1, 'symbol': Fore.RED + '○'},  # circle
    {'x': 40, 'y': 12, 'vx': -1, 'vy': -1, 'symbol': Fore.GREEN + '□'},  # square
    {'x': 20, 'y': 6, 'vx': 1, 'vy': -1, 'symbol': Fore.YELLOW + '△'},  # triangle
    {'x': 60, 'y': 18, 'vx': -1, 'vy': 1, 'symbol': Fore.BLUE + '⬠'},  # pentagon
    {'x': 30, 'y': 8, 'vx': 1, 'vy': 1, 'symbol': Fore.MAGENTA + '⬣'},  # hexagon
    
    {'x': 10, 'y': 4, 'vx': 1, 'vy': 1, 'symbol': Fore.GREEN + '○'},  # circle
    {'x': 50, 'y': 16, 'vx': -1, 'vy': -1, 'symbol': Fore.RED + '□'},  # square
    {'x': 70, 'y': 20, 'vx': 1, 'vy': -1, 'symbol': Fore.CYAN + '△'},  # triangle
    {'x': 20, 'y': 18, 'vx': -1, 'vy': 1, 'symbol': Fore.MAGENTA + '⬠'},  # pentagon
    {'x': 40, 'y': 12, 'vx': 1, 'vy': 1, 'symbol': Fore.WHITE + '⬣'},  # hexagon
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_screen():
    for line in screen:
        print(Back.BLACK + ''.join(line))
    print(Fore.RESET)

def update_screen():
    for y in range(height):
        for x in range(width):
            screen[y][x] = ' '
    
    for element in elements:
        screen[element['y']][element['x']] = element['symbol']

def update_elements():
    for element in elements:
        element['x'] += element['vx']
        element['y'] += element['vy']

        if element['x'] == width - 1:
            element['vx'] = -1
        elif element['x'] == 0:
            element['vx'] = 1

        if element['y'] == height - 1:
            element['vy'] = -1
        elif element['y'] == 0:
            element['vy'] = 1

while True:
    clear_screen()
    draw_screen()
    update_screen()
    update_elements()
    time.sleep(0.07)