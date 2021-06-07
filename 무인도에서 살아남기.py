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

stone2 = pygame.image.load("C:\\Users\\82104\\Desktop\\pygame\\이미지\\돌.png")
stone2 = pygame.transform.scale(stone2, (50, 50))
stone2_size = stone2.get_rect().size
stone2_width = stone2_size[0]
stone2_height = stone2_size[1]
stone2_xpos = 0
stone2_ypos = stone2_height

stone3 = pygame.image.load("C:\\Users\\82104\\Desktop\\pygame\\이미지\\돌.png")
stone3 = pygame.transform.scale(stone3, (50, 50))
stone3_size = stone3.get_rect().size
stone3_width = stone3_size[0]
stone3_height = stone3_size[1]
stone3_xpos = 0
stone3_ypos = stone3_height

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
stone3_speed = 1.3
fruit_speed = 1
clock = pygame.time.Clock()
character_speed = 0.5
to_x = 0
running = True
_running = True  #

bonus = 0

while _running:  #
    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= character_speed
                if event.key == pygame.K_RIGHT:
                    to_x += character_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
        character_xpos += to_x * dt

        if character_xpos < 0:
            character_xpos = 0
        elif character_xpos > screen_width - character_width:
            character_xpos = screen_width - character_width
        if character_ypos < 0:
            character_ypos = 0
        elif character_ypos > screen_height - character_height:
            character_ypos = screen_height - character_height
        if stone_ypos >= screen_height + 70 or stone_ypos == 70:
            stone_ypos = stone_height
            stone_xpos = random.uniform(0, screen_width - character_width)
        if fruit_ypos >= screen_height + 70 or fruit_ypos == 70:
            fruit_ypos = fruit_height
            fruit_xpos = random.uniform(0, screen_width - character_width)

        stone_ypos += stone_speed
        stone_speed += 0.02
        stone2_ypos += stone2_speed
        stone2_speed += 0.03
        stone3_ypos += stone3_speed
        stone3_speed += 0.008
        fruit_ypos += fruit_speed
        fruit_speed += 0.01

        character_rect = character.get_rect()
        character_rect.left = character_xpos
        character_rect.top = character_ypos

        stone_rect = character.get_rect()
        stone_rect.left = stone_xpos
        stone_rect.top = stone_ypos

        stone2_rect = character.get_rect()
        stone2_rect.left = stone2_xpos
        stone2_rect.top = stone2_ypos

        stone3_rect = character.get_rect()
        stone3_rect.left = stone3_xpos
        stone3_rect.top = stone3_ypos

        fruit_rect = character.get_rect()  #
        fruit_rect.left = fruit_xpos  #
        fruit_rect.top = fruit_ypos  #

        if character_rect.colliderect(stone_rect,):
            running = False
        if character_rect.colliderect(stone2_rect,):
            running = False
        if character_rect.colliderect(stone3_rect,):
            running = False

        if character_rect.colliderect(fruit_rect):
            bonus += 5
            fruit_ypos = fruit_height
            fruit_xpos = random.uniform(0, screen_width - character_width)
            screen.blit(fruit, (fruit_xpos, fruit_ypos))
            pygame.display.update()

        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_ticks) / 1000
        timer = game_font.render(str(int(elapsed_time+bonus)), True, (255, 255, 255))
        result = game_font.render(str(int(elapsed_time + bonus)), True, (0, 0, 0))
        test = game_font.render(str(int(bonus)), True, (255, 255, 255))

        screen.blit(background, (0, 0))
        screen.blit(character, (character_xpos, character_ypos))
        board_font = pygame.font.Font(None, 50)  #
        board = board_font.render("Score : ", True, (0, 0, 0))
        screen.blit(stone, (stone_xpos, stone_ypos))
        screen.blit(stone2, (stone2_xpos, stone2_ypos))
        screen.blit(stone3, (stone3_xpos, stone3_ypos))
        screen.blit(fruit, (fruit_xpos, fruit_ypos))
        screen.blit(board, (10, 10))
        screen.blit(result, (140, 16))
        pygame.display.update()

    score_font = pygame.font.Font(None, 50)  #
    text = score_font.render("your life day", True, (255, 255, 255))
    text_rect = text.get_rect()
    timer_rect = timer.get_rect()
    screen.fill((0, 0, 0))
    screen.blit(timer, (10, 50))  #
    screen.blit(text, (10, 10))  #
    pygame.display.update()  #
    for event in pygame.event.get():  #
        if event.type == pygame.QUIT:  #
            _running = False  #

pygame.quit()