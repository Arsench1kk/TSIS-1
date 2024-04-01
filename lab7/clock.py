import pygame
import datetime
pygame.init()
size = [1050, 800]
center = [525, 400]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

current_datetime = datetime.datetime.now()
seconds = current_datetime.second
minutes = current_datetime.minute

mickey1 = pygame.image.load("mainclock.png").convert_alpha()
mickey = pygame.transform.scale(mickey1, (1050, 800))

hour_arm1 = pygame.image.load("rightarm.png").convert_alpha()
hour_arm = pygame.transform.rotate((pygame.transform.scale(hour_arm1, (1050, 800))), -45)
hour_rect = hour_arm.get_rect(center = center)

def rotate_arm(image, angle, center):
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=center)
    screen.blit(rotated_image, rotated_rect)
angleminute=seconds*6
anglehour=minutes*6
counter=0

minute_arm1 = pygame.image.load("leftarm.png").convert_alpha()
minute_arm = pygame.transform.scale(minute_arm1, (63, 800))
minute_rect = minute_arm.get_rect(center = center)

rotate_arm(minute_arm, 0, center)
rotate_arm(hour_arm, 0, center)

screen.blit(mickey, (0, 0)) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    counter+=1
    if(counter==30):
        seconds+=1
        counter=0
        angleminute+=6

    if(seconds==60):
        minutes+=1
        seconds=0
        anglehour+=6
    
    if(minutes==60):
        minutes=0
    
    screen.blit(mickey, (0, 0))
    rotate_arm(hour_arm, anglehour, center)
    rotate_arm(minute_arm, angleminute, center)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()