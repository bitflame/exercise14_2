import pygame
running = True
pygame.init()
screen = pygame.display.set_mode((1200, 750))
display_rectangle = screen.get_rect()
clock = pygame.time.Clock()
rectShape = pygame.Rect(display_rectangle.right -120  ,2,100,5)
direction = 1
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('purple')
    pygame.draw.rect(screen,'black',rectShape)
    rectShape.y += 2 * direction
    if rectShape.y >= display_rectangle.bottom:
        direction = -1
    if rectShape.y <= 0: 
        direction = 1
    pygame.display.flip()
    clock.tick(60)
    

    
pygame.quit()
        