import random 
import pygame
import time
from pygame.locals import *

pygame.init()

def surf(color ,size):
	s = pygame.Surface(size)
	s.fill(color)
	return s
	
def grow():
	snake.append([])

def draw_snake():
	for b in snake:
		screen.blit( snake_body , b)

def move_snake():
	for i in range(1 ,len(snake)):
		x = (len(snake))-i
		snake[x] = snake[x-1].copy()

	if direction == "up" :
		snake[0][1] -= case_size
	elif direction == "right":
		snake[0][0] += case_size
	elif direction == "left":
		snake[0][0] -= case_size
	elif direction == "down":
		snake[0][1] += case_size
	
	head_x , head_y  = snake[0]
	if head_x < 0 or head_x >=400 or head_y < 0 or head_y >= 400:
		return False

	for i in range(1,len(snake)):
		if snake[0] == snake[i]:
			return False

	return True

def generate_apple():
	return [(random.randrange(0,40))*case_size ,(random.randrange(0, 40))*case_size]
#configuration
score = 0
case_size = 10
black = 0x000000
red = 0xff0000
screen_size = (400,400)
snake_body = surf(black, (case_size , case_size))
apple = surf(red, (case_size,case_size))
snake = [[i*10 ,int(screen_size[0]/2)] for i in range(10)]
snake.reverse()
screen = pygame.display.set_mode(screen_size)
title = pygame.display.set_caption("snake")
background = surf( 0xffffff  , screen.get_size())
apple_pos = generate_apple()
direction = "right"
clock = pygame.time.Clock()
score_font = pygame.font.Font(None , 16)
done = False
#main loop
while not done:
	screen.fill(0xffffff)
	screen.blit(apple , apple_pos)

	draw_snake()

	if snake[0]  == apple_pos :
		while apple_pos in snake :
			apple_pos = generate_apple()
		score+= 1
		grow()

	score_text = score_font.render(str(score) , False ,(0,0,0))
	screen.blit(score_text, (370,30))
	pygame.display.update()
	if move_snake() == False:
		done = True


	for event in pygame.event.get():
		if event.type == QUIT :
			done = True
		elif event.type == KEYDOWN:
			if event.key == K_UP and direction != "down":
				direction = "up"

			elif event.key == K_RIGHT and direction != "left":
				direction = "right"

			elif event.key == K_LEFT and direction != "right":
				direction = "left"

			elif event.key == K_DOWN and direction != "up":
				direction ="down"
	
	clock.tick(10)