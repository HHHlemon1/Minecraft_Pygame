import pygame,time

pygame.init()

clock = pygame.time.Clock()
clock.tick(60)
pygame.display.set_caption("Minecraft")
win_height, win_width = 1080, 1920
player_height, player_width = 60, 40
player_speed = 10
win = pygame.display.set_mode((win_width, win_height))
g = 9.8*0.02
tickgone = 0
statu = "drop"


class player:
    def __init__(self):
        self.player_rect = pygame.Rect(win_width//2, win_height//2, player_width, player_height)
        self.speed = player_speed
    def move(self, keys):
        if keys[pygame.K_a] and not self.player_rect.left < win_width//3.5:
            self.player_rect.x -= self.speed
        if keys[pygame.K_d] and not self.player_rect.right > win_width//1.4:
            self.player_rect.x += self.speed
    def drop(self, keys):
        global tickgone
        global statu
        if statu == "drop":
            tickgone += 1
            if self.player_rect.bottom < win_height//1.5:
                self.player_rect.y += tickgone*g
                if keys[pygame.K_s]:
                    self.player_rect.y += (tickgone*g+10)
            else:
                Blocks.y_scroll()
    def jump(self, keys):
        global tickgone
        global statu
        if keys[pygame.K_w] and statu == "common":
            statu = "jump"
        if statu == "jump":
            if (self.speed*0.8 - tickgone*g) > 0:
                tickgone += 1
                self.player_rect.y -= (self.speed*0.8 - tickgone*g)
            else:
                tickgone = 0
                statu = "drop"
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.player_rect)

class blocks:
    def __init__(self):

        self.speed = player_speed
        self.blocks_list=[]
        for n in range(60):
            x = 40*n
            y = 800
            self.block = pygame.Rect(x, y, 40, 40)
            self.blocks_list.append(self.block)
        for n in range(20):
            x = 40*n
            y = 650
            self.block = pygame.Rect(x, y, 40, 40)
            self.blocks_list.append(self.block)
    def collison(self):
        global statu
        global tickgone
        self.collided = False
        for block in self.blocks_list:
            if Player.player_rect.colliderect(block):
                self.collided = True
                #if Player.player_rect.top >= block.top + 40:
                Player.player_rect.bottom = block.top
                break
        if self.collided == True:
            statu = "common" 
            tickgone = 0
        elif not statu == "jump":
            statu = "drop"
        
    def x_scroll(self, keys):
        for block in self.blocks_list:
            if keys[pygame.K_a] and Player.player_rect.left < win_width//3.5:
                block.x += self.speed
            if keys[pygame.K_d] and Player.player_rect.right > win_width//1.4:
                block.x -= self.speed
    def y_scroll(self):
        for block in self.blocks_list:
            block.y -= tickgone*g
    def draw(self, surface):
        for block in self.blocks_list:
            pygame.draw.rect(surface, (135, 99, 0), block)
            
Player = player()
Blocks = blocks()

running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    wordtime = time.time()
    #Fill background
    win.fill((135, 206, 235))
    keys = pygame.key.get_pressed()
    Player.move(keys)
    Player.drop(keys)
    Player.jump(keys)
    Blocks.x_scroll(keys)
    Blocks.collison()
    Player.draw(win)
    Blocks.draw(win)
    pygame.display.flip()
pygame.quit()
