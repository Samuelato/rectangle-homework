import pygame
import time
pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("birthday")

imag=pygame.image.load("images/bg.jpg")
siz=pygame.transform.scale(imag,(WIDTH,HEIGHT))

font=pygame.font.SysFont("Times New Roman",77)
tex=font.render("happy birthday",True,(0,0,0))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(siz,(0,0))
    screen.blit(tex,(100,100))

    pygame.display.update()
    time.sleep(2)

    imaf=pygame.image.load("images/img2.jpg")
    screen.blit(imaf,(0,0))
    pygame.display.update()
    time.sleep(2)
    running=False
pygame.quit()