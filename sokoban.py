#Name: pySokoban
# Description: A sokoban implementation using python & pyGame
# Author: Kazantzakis Nikos <kazantzakisnikos@gmail.com>
# Date: 2015

import pygame
import time
import sys
from pathlib import Path
from Environment import Environment
from Level import Level

def drawLevel(matrix_to_draw):

    # Load level images
    image_dir       = Path(myEnvironment.get_app_dir()) / 'themes' / theme / 'images'
    wall            = pygame.image.load(image_dir / 'wall.png').convert()
    box             = pygame.image.load(image_dir / 'box.png').convert()
    box_on_target   = pygame.image.load(image_dir / 'box_on_target.png').convert()
    space           = pygame.image.load(image_dir / 'space.png').convert()
    target          = pygame.image.load(image_dir / 'target.png').convert()
    player          = pygame.image.load(image_dir / 'player.png').convert()

    # If horizontal or vertical resolution is not enough to fit the level images then resize images
    if myLevel.getSize()[0] > myEnvironment.size[0] // 36 or myLevel.getSize()[1] > myEnvironment.size[1] // 36:

        # If level's x size > level's y size then resize according to x axis
        if myLevel.getSize()[0] / myLevel.getSize()[1] >= 1:
            new_image_size = myEnvironment.size[0] // myLevel.getSize()[0]
        # If level's y size > level's x size then resize according to y axis
        else:
            new_image_size = myEnvironment.size[1] // myLevel.getSize()[1]

        # Just to the resize job
        wall = pygame.transform.scale(wall, (new_image_size,new_image_size))
        box = pygame.transform.scale(box, (new_image_size,new_image_size))
        box_on_target = pygame.transform.scale(box_on_target, (new_image_size,new_image_size))
        space = pygame.transform.scale(space, (new_image_size,new_image_size))
        target = pygame.transform.scale(target, (new_image_size,new_image_size))
        player = pygame.transform.scale(player, (new_image_size,new_image_size))

    # Just a Dictionary (associative array in pyhton's lingua) to map images to characters used in level design
    images = {'#': wall, ' ': space, '$': box, '.': target, '@': player, '*': box_on_target, '+': player}

    # Get image size. Images are always squares so it doesn't care if you get width or height
    box_size = wall.get_width()

    # Iterate all Rows
    for i in range (0,len(matrix_to_draw)):
        # Iterate all columns of the row
        for c in range (0,len(matrix_to_draw[i])):
            myEnvironment.screen.blit(images[matrix_to_draw[i][c]], (c*box_size, i*box_size))

    pygame.display.update()

def movePlayer(dx, dy, myLevel):

    # Get the level's matrix...
    matrix = myLevel.getMatrix()

    # Where we are now...
    x, y = myLevel.getPlayerPosition()

    # Where we want to go...
    next_x, next_y = x + dx, y + dy

    # What's there...
    next_cell = matrix[next_y][next_x]

    # Position of the cell behind a potential box...
    box_next_x, box_next_y = x + 2*dx, y + 2*dy

    # What's there...
    box_next_cell = matrix[box_next_y][box_next_x] if next_cell in ("$", "*") else None

    print(f"######### Moving ({dx},{dy}) #########")

    # Invalid moves — no history recorded
    if next_cell == "#":
        print("There is a wall here")
        return
    if next_cell in ("$", "*") and box_next_cell not in (" ", "."):
        print("Box cannot be pushed")
        return

    # Valid move — record history
    myLevel.addToHistory(matrix)

    def update_current_cell():
        matrix[y][x] = "." if matrix[y][x] == "+" else " "

    if next_cell == " ":
        print("OK Space Found")
        matrix[next_y][next_x] = "@"
        update_current_cell()

    elif next_cell == "$":
        print("Box Found")
        matrix[box_next_y][box_next_x] = "$" if box_next_cell == " " else "*"
        matrix[next_y][next_x] = "@"
        update_current_cell()

    elif next_cell == "*":
        print("Box on target Found")
        matrix[box_next_y][box_next_x] = "$" if box_next_cell == " " else "*"
        matrix[next_y][next_x] = "+"
        update_current_cell()

    elif next_cell == ".":
        print("Target Found")
        matrix[next_y][next_x] = "+"
        update_current_cell()

    drawLevel(matrix)

    print("Boxes remaining: " + str(len(myLevel.getBoxes())))

    if len(myLevel.getBoxes()) == 0:
        myEnvironment.screen.fill((0, 0, 0))
        print("Level Completed")
        global current_level
        current_level += 1
        initLevel(level_set, current_level)

def initLevel(level_set,level):
    # Create an instance of this Level
    global myLevel
    myLevel = Level(level_set,level)

    x, y = myLevel.getPlayerPosition()

    print(x, y)

    # Draw this level
    drawLevel(myLevel.getMatrix())


# Create the environment
myEnvironment = Environment()

# Choose a theme
theme = "default"

# Choose a level set
level_set = "magic_sokoban6"

# Set the start Level
current_level = 53

# Initialize Level
initLevel(level_set,current_level)

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movePlayer(-1, 0, myLevel)
            elif event.key == pygame.K_RIGHT:
                movePlayer( 1, 0, myLevel)
            elif event.key == pygame.K_DOWN:
                movePlayer( 0, 1, myLevel)
            elif event.key == pygame.K_UP:
                movePlayer( 0,-1, myLevel)
            elif event.key == pygame.K_u:
                drawLevel(myLevel.getLastMatrix())
            elif event.key == pygame.K_r:
                initLevel(level_set,current_level)
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
