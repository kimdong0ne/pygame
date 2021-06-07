import pygame
import random

pygame.init()

background = pygame.image.load("C:\\Users\\82104\\Desktop\\pygame\\이미지\\무인도.png")
pygame.display.set_caption("무인도에서 살아남기")
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

character = pygame.image.load("C:\\Users\\82104\\Desktop\\pygame\\이미지\\사람.png")
character = pygame.transform.scale(character, (50, 50))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = screen_width / 2 - character_width / 2
character_ypos = screen_height - character_height

stone = pygame.image.load("C:\\Users\\82104\\Desktop\\pygame\\이미지\\돌.png")
stone = pygame.transform.scale(stone, (50, 50))
stone_size = stone.get_rect().size
stone_width = stone_size[0]
stone_height = stone_size[1]
stone_xpos = 0
stone_ypos = stone_height

stone2 = pygame.image.load("C:\\Users\\82104\\Desktop\\pygame\\이미지\\돌2.png")
stone2 = pygame.transform.scale(stone, (50, 50))
stone2_size = stone2.get_rect().size
stone2_width = stone2_size[0]
stone2_height = stone2_size[1]
stone2_xpos = 0
stone2_ypos = stone2_height

fruit = pygame.image.load("C:\\Users\\82104\\Desktop\\pygame\\이미지\\바나나.png")
fruit = pygame.transform.scale(fruit, (50, 50))
fruit_size = fruit.get_rect().size
fruit_width = fruit_size[0]
fruit_height = fruit_size[1]
fruit_xpos = 0
fruit_ypos = fruit_height

start_ticks = pygame.time.get_ticks()

game_font = pygame.font.Font(None, 40)

stone_speed = 1.1
stone2_speed = 0.8
fruit_speed = 1
clock = pygame.time.Clock()
character_speed = 0.5
to_x = 0
running = True
_running = True  #

bonus = 0