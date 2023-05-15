import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
running = True
GREEN = (0, 200, 0)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
clock = pygame.time.Clock()
circle_color = RED


font = pygame.font.SysFont('sans',30) # create font 
text = font.render("Random",True,BLACK)# tao chu Random 
text_box = text.get_rect() #get positon of text "Random",return tuple [0,0,length,width]

random_pos = (50,50)

while running:
    clock.tick(60)
    screen.fill(WHITE)
    
    mouse_x, mouse_y = pygame.mouse.get_pos() #get mouse position
     
    pygame.draw.rect(screen,WHITE,(random_pos[0],random_pos[1],text_box[2],text_box[3]))
    pygame.draw.circle(screen, circle_color, (200,300),50) # draw circle
    screen.blit(text,random_pos) #draw text on screen
    if (random_pos[0] < mouse_x < random_pos[0]+text_box[2]) and (random_pos[1] < mouse_y < random_pos[1]+ text_box[3]):
                text = font.render("Random",True,BLUE)
                pygame.draw.line(screen,BLUE,(random_pos[0],random_pos[1]+text_box[3]),(random_pos[0]+ text_box[2],random_pos[1]+text_box[3]))
    else:
                text = font.render("Random",True,BLACK)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: #check mouse click
             if (random_pos[0] < mouse_x < random_pos[0]+text_box[2]) and (random_pos[1] < mouse_y < random_pos[1]+ text_box[3]):
                text = font.render("Random",True,RED)
                if event.button == 1: #check right click
                    circle_color = (randint(0,255),randint(0,255),randint(0,255))
                    print("left click")
            
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()