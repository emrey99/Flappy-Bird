import pygame
import random

pygame.init()

SCREEN = pygame.display.set_mode((664,665))

BACKGROUND_IMAGE = pygame.image.load('C:/Users/Acer/Desktop/newflap.png ')
pygame.display.set_icon(BACKGROUND_IMAGE)


BIRD_IMG = pygame.image.load('C:/Users/Acer/Desktop/bird1.png')
pygame.display.set_icon(BIRD_IMG)
bird_x = 50
bird_y = 300
bird_y_change = 0

def display_bird(x,y):
    SCREEN.blit(BIRD_IMG , (x,y))

OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = random.randint(100,370)
OBSTACLE_COLOR = (255, 0, 0)
OBSTACLE_X_CHANGE = -1.5
obstacle_x = 664

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR,(obstacle_x, 0 ,OBSTACLE_WIDTH,height))
    bottom_obstacle_height = 570- height - 150
    starting_point_second_obstacle = height + 150

    pygame.draw.rect(SCREEN, OBSTACLE_COLOR,(obstacle_x,starting_point_second_obstacle,OBSTACLE_WIDTH,bottom_obstacle_height))

def collision_detection(obstacle_x,obstacle_height,bird_y,bottom_obstacle_height):
    if obstacle_x <=50:
        if bird_y <= obstacle_height or bird_y >= obstacle_height + 125:
            return True
    return False


running = True
while running:

    SCREEN.fill((0,0,0))

    SCREEN.blit(BACKGROUND_IMAGE, (0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 1


    bird_y += bird_y_change



    if bird_y <=0:
        bird_y =0
    if bird_y >= 533:
        bird_y = 533

    obstacle_x += OBSTACLE_X_CHANGE
    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(100,370)
    display_obstacle(OBSTACLE_HEIGHT)

    collision = collision_detection(obstacle_x,OBSTACLE_HEIGHT,bird_y,OBSTACLE_HEIGHT + 100)

    if collision:
        pygame.quit()

    display_bird(bird_x,bird_y)

    pygame.display.update()


pygame.quit()
