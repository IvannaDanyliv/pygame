import pygame
pygame.init()
import time
window = pygame.display.set_mode((500,500))
window.fill((0, 255, 229))
clock=pygame.time.Clock()
clock.tick(280)
racket_x =200
racket_y =330
game_over=False
speed_x=3
speed_y=3
class Area():
    def __init__(self,x=0,y=0, width=10,height=10,  color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color=new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def outline(self,frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.ract.colliderect(rect)
class Picture(Area):
    def __init__(self,x=0,y=0, width=10,height=10,  color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def draw(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
ball=Picture("ball.png", racket_x, racket_y,100,30)
platform=Picture("platform.png", racket_x, racket_y, 150, 50)
#створення ворогів
start_x=5
start_y=5
count=9
monsters=[]
for j in range(3):
    y = start_y + (55* j)
    x = start_x + (27.5* j)
    for i in range(count):
        d = Picture ("enemy.png", x, y,50,50)
        monsters.append(d)
        x = x +55
    count = count -1
while not game_over:
    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event .type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                move_right=True
                if move_right:
                    platform.rect.x +=3
    for event in pygame.event.get():
        if event .type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                move_left=True
                if move_left:
                    platform.rect.x -=3
    ball.rect.x += speed_x
    ball.rect.t += speed_y
    if ball.colliderect(platform.rect):
        speed_y *=-1
    for m in monsters:
        m.draw()
