from ast import If
import pygame, os
# 1280 x 720, 1920,1080
width, height = 1000, 680
win = pygame.display.set_mode((width, height))
white = (255,255,255)
black = (0,0,0)
pygame.display.set_caption("Shooting game")
bullet_vel = 10
border = pygame.Rect(500-2.5, 0, 5, height)

# yellow spaceship
yellow_spaceship = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))
yellow_spaceship_size = pygame.transform.rotate(
    pygame.transform.scale(yellow_spaceship,(75,60)),
                                                90)
# red spaceship
red_spaceship = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png"))
red_spaceship_size = pygame.transform.rotate(
    pygame.transform.scale(red_spaceship,(75,60)),
                                            270)

def draw(red, ylw):
    win.fill(white)
    pygame.draw.rect(win, black, border)
    win.blit(yellow_spaceship_size,(ylw.x, ylw.y))
    win.blit(red_spaceship_size,(red.x, red.y))
    pygame.display.update()

def yellow_movement_handler(keys_pressed, yellow):
    if keys_pressed[pygame.K_w] and yellow.y - 15 > 0:
        yellow.y -= 5
    if keys_pressed[pygame.K_s] and yellow.y + yellow.height + 20 < height:
        yellow.y += 5
    if keys_pressed[pygame.K_a] and yellow.x - 15 > 0:
        yellow.x -= 5
    if keys_pressed[pygame.K_d] and yellow.x + yellow.width + 15 < border.x:
        yellow.x += 5

def red_movement_handler(keys_pressed, red):
    if keys_pressed[pygame.K_UP] and red.y - 15 > 0:
        red.y -= 5
    if keys_pressed[pygame.K_DOWN] and red.y + red.height + 20 < height:
        red.y += 5
    if keys_pressed[pygame.K_LEFT] and red.x - 25 > border.x:
        red.x -= 5
    if keys_pressed[pygame.K_RIGHT] and red.x + red.width - 5 < width:
        red.x += 5

def main():
    red  = pygame.Rect(800, 300, 75, 60)
    yellow = pygame.Rect(200, 300, 75, 60)
    yellow_bullets = []
    red_bullets = []
    clock = pygame.time.Clock()
    run = True
    while bool(run):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Code starts here
            if event.type == pygame.KEYDOWN:
                # Yellow bullet
                if event.key == pygame.K_LCTRL:
                    yellow_x = yellow.x + yellow.width
                    yellow_y = yellow.y + yellow.height / 2
                    yellow_bullet = pygame.Rect(yellow_x, yellow_y, 10, 5)
                    yellow_bullets.append(yellow_bullet)
                # Red bullet
                if event.key == pygame.K_RCTRL:
                    red_y = red.y + red.height / 2
                    red_bullet = pygame.Rect(red.x, red_y, 10, 5)
                    red_bullets.append(red_bullet)
                    
        keys_pressed = pygame.key.get_pressed()
        yellow_movement_handler(keys_pressed, yellow)
        red_movement_handler(keys_pressed, red)
        draw(red, yellow)


    pygame.quit()

"   *************************************************************    "


if __name__ == '__main__':
    main()