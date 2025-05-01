import pygame

pygame.init()
resolution = (1920,1080)
win = pygame.display.set_mode(resolution)
pygame.display.set_caption("Minecraft")

player_width,player_height = 40,60



class player:
    def __init__(self):
        

print("Hello Minecraft")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    win.fill((135, 206, 235))

    # Get pressed keys
    #keys = pygame.key.get_pressed()

    # Move and draw the player
    #player.move(keys)
    #player.draw(win)

    pygame.display.flip()

pygame.quit()