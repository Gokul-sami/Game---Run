import pygame
import random

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("RUN!!!")
screen.fill((255,255,255))
print(screen)

x = y = 350
z1 = 350
z2 = 656
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
			elif event.key == pygame.K_LEFT:
				x -= 5
			elif event.key == pygame.K_RIGHT:
				x += 5
			elif event.key == pygame.K_UP:
				y -= 5
			elif event.key == pygame.K_DOWN:
				y += 5
			
	pygame.draw.rect(screen,(0,0,0),(0,0,700,700))
	pygame.draw.circle(screen,(0,255,0),(x,y),10)
	
	if ((x > z1) and (y < z2)):
		z1 += 0.1
		z2 -= 0.1
	elif ((x < z1) and (y < z2)):
		z1 -= 0.1
		z2 -= 0.1
	elif ((x > z1) and (y > z2)):
		z1 += 0.1
		z2 += 0.1
	elif ((x == z1) and (y > z2)):
		z2 += 0.1
	elif ((y == z2) and (x < z1)):
		z1 -= 0.1
	elif ((y == z2) and (x > z1)):
		z1 += 0.1
	elif ((x == z1) and (y < z2)):
		z2 -= 0.1
	else:
		z1 -= 0.1
		z2 += 0.1	
	pygame.draw.circle(screen,(255,0,0),(z1,z2),10)
	
	if (x==z1 and y==z2):
		pygame.quit()
	
	pygame.display.update()