import pygame
import sys
from pygame.locals import *
import random
from random import randint
from buttonCode import Button

'''
'''

pygame.init()

#basic setup
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#all the variables
seconds = 0
highscore = 0



#player creation
player_surf = pygame.Surface((100,100))
player_rect = player_surf.get_rect(center = (400,600))

#Global images

background=pygame.image.load('background copy.jpeg').convert_alpha()
background=pygame.transform.scale(background,(width,height))


#sounds
death=pygame.mixer.Sound('medium-explosion-40472.mp3')
pygame.mixer.music.load('beyond-infinity-159345.mp3')
warning=pygame.mixer.Sound('correct-choice-43861.mp3')
blaster=pygame.mixer.Sound('laser-shot-ingame-230500 (1).mp3')
damage=pygame.mixer.Sound('jump-climb-or-damage-sound-f-95942.mp3')
pygame.mixer.music.play(-1)

#font creation
font = pygame.font.SysFont(None, 34)
font2 = pygame.font.SysFont(None, 64)
font3 = pygame.font.SysFont(None, 37)
time_text = font.render("Time:", True, (255,255,255))
seconds_text = font.render(f"{seconds}", True, (255,255,255))
highscore_text = font.render(f"{highscore} seconds", True, (255,255,255))
reset_text = font.render("Press R to Reset Game.", True, (255,255,255))
Game_Over = font2.render("Game Over!!!", True, (255,255,255))
Level_Complete = font2.render("Level Complete!!", True, (255,255,255))
time_taken_text = font2.render(f"{seconds} Seconds", True, (255,255,255))


def get_font(size):
    return pygame.font.Font(None, size)

def play():  # play screen
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    # all the variables
    start_timer = 0
    start = 0
    enemyhealth = 5
    starting_health = 5
    minionhealth = 1
    enemyspawn = 5
    deathcount = 0
    bossspawn = 1
    complete = 0
    timetaken = 0
    reset = 0
    seconds = 0
    highscore = 0
    counter = 0
    timetillmove = 0
    movementchoice = 0
    countdown = 120
    Dead = False
    started = False
    astroid_surf_store = []
    astroid_rect_store = []
    astroid_move_store = []
    enemy_rect_store = []
    enemy_image_store = []
    enemy_move_store = []
    movementlist = []
    fire_rect_list = []
    fire_image_list = []
    hp_list = []

    # player creation
    player_surf = pygame.Surface((70, 70))
    player_rect = player_surf.get_rect(center=(400, 600))

    # boss creation
    enemy = pygame.Rect(5, 10, 50, 100)
    enemysurf = pygame.Surface((50, 100))

    # boss fire creation
    fire = pygame.Rect(enemy.x + 15, enemy.y, 20, 20)

    # laser variable creation
    lasers = []
    laser_speed = 10
    laser_width, laser_height = 10, 10
    laser_color = (255, 0, 0)

    # images
    laser_image = pygame.image.load('blast.png').convert_alpha()
    bosslaser = pygame.transform.scale(laser_image, (20, 20))
    enemylaser = pygame.transform.scale(laser_image, (20, 20))
    enemylaser = pygame.transform.rotate(enemylaser, 180)
    boss_image = pygame.image.load('rocket-6972424_1280.png').convert_alpha()
    player_image = pygame.image.load('playerShip.png').convert_alpha()
    boss_image = pygame.transform.scale(boss_image, (50, 100))
    boss_image = pygame.transform.rotate(boss_image, 180)
    player_image = pygame.transform.scale(player_image, (90, 90))
    background = pygame.image.load('background copy.jpeg').convert_alpha()
    background = pygame.transform.scale(background, (width, height))

    # sounds
    death = pygame.mixer.Sound('medium-explosion-40472.mp3')
    pygame.mixer.music.load('beyond-infinity-159345.mp3')
    warning = pygame.mixer.Sound('correct-choice-43861.mp3')
    blaster = pygame.mixer.Sound('laser-shot-ingame-230500 (1).mp3')
    damage = pygame.mixer.Sound('jump-climb-or-damage-sound-f-95942.mp3')
    pygame.mixer.music.play(-1)

    # font creation
    font = pygame.font.SysFont(None, 34)
    font2 = pygame.font.SysFont(None, 64)
    font3 = pygame.font.SysFont(None, 37)
    time_text = font.render("Time:", True, (255, 255, 255))
    seconds_text = font.render(f"{seconds}", True, (255, 255, 255))
    highscore_text = font.render(f"{highscore} seconds", True, (255, 255, 255))
    reset_text = font.render("Press R to Reset Game.", True, (255, 255, 255))
    Game_Over = font2.render("Game Over!!!", True, (255, 255, 255))
    Level_Complete = font2.render("Level Complete!!", True, (255, 255, 255))
    time_taken_text = font2.render(f"{seconds} Seconds", True, (255, 255, 255))

    # just all the methods
    # quit method
    def checkQuit():
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                laser = pygame.Rect(player_rect.centerx, player_rect.y+20, laser_width, laser_height)
                lasers.append(laser)
                if started == True and reset == 0:
                    blaster.play()
            elif keys[pygame.K_SPACE]:
                if countdown % 10 == 0:
                    laser = pygame.Rect(player_rect.centerx, player_rect.y+20, laser_width,
                                        laser_height)
                    lasers.append(laser)
                    if started == True and reset == 0:
                        blaster.play()

    # boss movement method
    def movement(movementchoice, enemy):
        if movementchoice == 0 and enemy.x <= 750:
            return enemy.move(1, 0)
        elif movementchoice == 0:
            return enemy.move(0, 0)
        if movementchoice == 1 and (enemy.y <= 300):
            return enemy.move(0, 1)
        elif movementchoice == 1:
            return enemy.move(0, 0)
        if movementchoice == 2 and (enemy.x >= 0):
            return enemy.move(-1, 0)
        elif movementchoice == 2:
            return enemy.move(0, 0)
        if movementchoice == 3 and (enemy.y >= 0):
            return enemy.move(0, -1)
        elif movementchoice == 3:
            return enemy.move(0, 0)

    # boss blaster/laser movement
    def firerate(countdown, fire, enemy):
        if countdown >= 120:
            blaster.play()
            return pygame.Rect(enemy.x + 15, enemy.y + 30, 20, 20)
        if enemy.w < enemy.h and enemy.y < 250:
            return fire.move(0, 15)
        elif enemy.w < enemy.h and enemy.y >= 250:
            return fire.move(0, 15)
        if enemy.w > enemy.h and enemy.x < 350:
            return fire.move(0, 15)
        elif enemy.w > enemy.h and enemy.x >= 350:
            return fire.move(0, 15)

    # all other enemy fire
    def firemove(countdown, fire_rect_list, enemy_rect_store):
        if countdown >= 120:
            blaster.play()
            for i in range(len(enemy_rect_store)):
                fire_rect_list[i] = pygame.Rect(enemy_rect_store[i].x + 32, enemy_rect_store[i].y + 30, 10, 10)
        for i in range(len(enemy_rect_store)):
            fire_rect_list[i] = fire_rect_list[i].move(0, 20)
        return fire_rect_list

    # makes asteroids pls don't touch I can't fix if you fully break
    def make_astroid(astroid_rect_store, astroid_surf_store, astroid_move_store):
        size = randint(20, 60)
        astroid = pygame.Surface((size, size))
        asteroid_image = pygame.image.load('asteriod.png').convert_alpha()
        asteroid_image = pygame.transform.scale(asteroid_image, (size, size))
        astroid_rect = astroid.get_rect()
        astroid.fill((255, 0, 0))
        start_side = randint(1, 4)
        if start_side == 1:
            x_coord = randint(0, 740)
            astroid_rect.topleft = (x_coord, -30)
            move = (0, randint(5, 10))
        if start_side == 2:
            x_coord = randint(0, 740)
            astroid_rect.topleft = (x_coord, 740)
            move = (0, randint(-10, -5))
        if start_side == 3:
            y_coord = randint(0, 740)
            astroid_rect.topleft = (10, y_coord)
            move = (randint(5, 10), 0)
        if start_side == 4:
            y_coord = randint(0, 740)
            astroid_rect.topleft = (740, y_coord)
            move = (randint(-10, -5), 0)
        astroid_surf_store.append(asteroid_image)
        astroid_rect_store.append(astroid_rect)
        astroid_move_store.append(move)
        return astroid_rect_store, astroid_surf_store, astroid_move_store

    # moves asteroids pls don't touch I can't fix if you fully break
    def astroid_move(astroid_move_store, astroid_rect_store):
        for i in range(len(astroid_rect_store)):
            astroid_rect_store[i].move_ip(astroid_move_store[i])
        return astroid_move_store, astroid_rect_store

    # makes the enemies. Seriously don't touch unless you understand fully I'd prefer you call me(Joshua) before touching this at all
    def make_enemy(enemy_rect_store, enemy_image_store, enemy_spawns, movementlist, fire_rect_list, fire_image_list,
                   hp):
        spawned = 0
        while enemy_spawns > spawned:
            x_coord = randint(0, 740)
            enemy = pygame.Surface((74, 60))
            enemy_image = pygame.image.load('EnemyShip.png').convert_alpha()
            enemy_image = pygame.transform.scale(enemy_image, (74, 60))
            fire = pygame.Surface((10, 10))
            laser_image = pygame.image.load('blast.png').convert_alpha()
            enemylaser = pygame.transform.scale(laser_image, (15, 15))
            fire_rect = fire.get_rect()
            fire.fill((255, 0, 0))
            fire_rect.topleft = (x_coord + 32, 40)
            movements = randint(0, 3)
            enemy_rect = enemy.get_rect()
            enemy_rect.topleft = (x_coord, 0)
            enemy.fill((0, 255, 0))
            enemy_image_store.append(enemy_image)
            enemy_rect_store.append(enemy_rect)
            movementlist.append(movements)
            fire_image_list.append(enemylaser)
            fire_rect_list.append(fire_rect)
            hp_list.append(hp)
            spawned += 1

        return enemy_rect_store, enemy_image_store, movementlist, fire_rect_list, fire_image_list, hp_list

    # makes enemies moves
    def enemy_movement(enemy_rect_store, movementlist):
        for i in range(len(enemy_rect_store)):
            if movementlist[i] == 0 and enemy_rect_store[i].x <= 740:
                enemy_rect_store[i] = enemy_rect_store[i].move(1, 0)
            elif movementlist[i] == 0:
                enemy_rect_store[i] = enemy_rect_store[i].move(0, 0)
            if movementlist[i] == 1 and (enemy_rect_store[i].y <= 300):
                enemy_rect_store[i] = enemy_rect_store[i].move(0, 1)
            elif movementlist[i] == 1:
                enemy_rect_store[i] = enemy_rect_store[i].move(0, 0)
            if movementlist[i] == 2 and (enemy_rect_store[i].x >= 0):
                enemy_rect_store[i] = enemy_rect_store[i].move(-1, 0)
            elif movementlist[i] == 2:
                enemy_rect_store[i] = enemy_rect_store[i].move(0, 0)
            if movementlist[i] == 3 and (enemy_rect_store[i].y >= 0):
                enemy_rect_store[i] = enemy_rect_store[i].move(0, -1)
            elif movementlist[i] == 3:
                enemy_rect_store[i] = enemy_rect_store[i].move(0, 0)
        return enemy_rect_store

    enemy_rect_store, enemy_image_store, movementlist, fire_rect_list, fire_image_list, hp_list = make_enemy(
        enemy_rect_store, enemy_image_store, enemyspawn, movementlist, fire_rect_list, fire_image_list, minionhealth)

    # game start
    while True:
        # basic setup
        if reset != 1 and started == True:
            if start < 20:
                for i in range(len(fire_rect_list)):
                    fire_rect_list[i] = fire_rect_list[i].move(800, 800)
            start += 1

        checkQuit()
        keys = pygame.key.get_pressed()
        screen.fill(color=(0, 0, 0))
        screen.blit(background, (0, 0))

        # button controls
        if keys[pygame.K_w]:
            if player_rect.topleft[1] == 0:
                player_rect.move_ip(0, 0)
            else:
                player_rect.move_ip(0, -5)
        if keys[pygame.K_s]:
            if player_rect.bottomleft[1] == height:
                player_rect.move_ip(0, 0)
            else:
                player_rect.move_ip(0, 5)
        if keys[pygame.K_a]:
            if player_rect.topleft[0] == 0:
                player_rect.move_ip(0, 0)
            else:
                player_rect.move_ip(-5, 0)
        if keys[pygame.K_d]:
            if player_rect.topright[0] == width:
                player_rect.move_ip(0, 0)
            else:
                player_rect.move_ip(5, 0)
        # makes it so you can only reset on certain screen
        if reset == 1:
            fire = pygame.Rect(810, 810, 20, 20)
            screen.blit(bosslaser, fire)
            for laser in lasers[:]:
                lasers.remove(laser)
            for z in range(len(fire_rect_list)):
                fire_rect_list[z] = pygame.Rect(810, 810, 10, 10)
                screen.blit(fire_image_list[z], fire_rect_list[z])
            # the reset button configuration
            if keys[pygame.K_r]:
                warning.play()
                astroid_rect_store = []
                astroid_surf_store = []
                astroid_move_store = []
                enemy_rect_store = []
                enemy_image_store = []
                enemy_move_store = []
                movementlist = []
                fire_rect_list = []
                fire_image_list = []
                hp_list = []
                start_timer = 0
                start = 0
                seconds = 0
                Dead = False
                reset = 0
                for laser in lasers[:]:
                    lasers.remove(laser)
                enemy_rect_store, enemy_image_store, movementlist, fire_rect_list, fire_image_list, hp_list = make_enemy(
                    enemy_rect_store, enemy_image_store, enemyspawn, movementlist, fire_rect_list, fire_image_list,
                    minionhealth)
                enemy = pygame.Rect(randint(0, 750), 10, 50, 100)
                enemysurf = pygame.Surface((50, 100))
                bossspawn = 1
                enemyhealth = starting_health
                complete = 0
                timetaken = 0
                player_rect = player_surf.get_rect(center=(400, 600))
        # makes a start screen
        if started == False:
            astroid_rect_store = []
            astroid_surf_store = []
            astroid_move_store = []
            player_rect = player_surf.get_rect(center=(900, 900))
            for z in range(len(fire_rect_list)):
                fire_rect_list[z] = pygame.Rect(810, 810, 10, 10)
                screen.blit(fire_image_list[z], fire_rect_list[z])
            fire = pygame.Rect(810, 810, 20, 20)
            screen.blit(bosslaser, fire)
            for j in range(len(enemy_rect_store)):
                enemy_rect_store[j].x = 800
                enemy_rect_store[j].y = 800
                screen.blit(enemy_image_store[j], enemy_rect_store[j])
            enemy = pygame.Rect(800, 800, 50, 100)
            started = True
            warning.play()
            seconds = 0
            astroid_rect_store = []
            astroid_surf_store = []
            astroid_move_store = []
            enemy_rect_store = []
            enemy_image_store = []
            enemy_move_store = []
            movementlist = []
            fire_rect_list = []
            fire_image_list = []
            hp_list = []
            Dead = False
            reset = 0
            for laser in lasers[:]:
                lasers.remove(laser)
            enemy_rect_store, enemy_image_store, movementlist, fire_rect_list, fire_image_list, hp_list = make_enemy(
                enemy_rect_store, enemy_image_store, enemyspawn, movementlist, fire_rect_list, fire_image_list,
                minionhealth)
            enemy = pygame.Rect(randint(0, 750), 10, 50, 100)
            enemysurf = pygame.Surface((50, 100))
            bossspawn = 1
            enemyhealth = starting_health
            complete = 0
            timetaken = 0
            player_rect = player_surf.get_rect(center=(400, 600))


        # not sure if this can be moved or not
        counter += 1
        # moves asteroids
        astroid_move_store, astroid_rect_store = astroid_move(astroid_move_store, astroid_rect_store)

        # blits all asteroids
        for i in range(len(astroid_rect_store)):
            screen.blit(astroid_surf_store[i], astroid_rect_store[i])

        # keeps track of enemy hp
        for j in range(len(enemy_rect_store)):
            if hp_list[j] <= 0:
                deathcount += 1
            if hp_list[j] <= 0:
                enemy_rect_store[j].x = 800
                enemy_rect_store[j].y = 800
            screen.blit(enemy_image_store[j], enemy_rect_store[j])

        # randomizes movements every 100 frames
        if timetillmove >= 100:
            timetillmove = 0
            movementchoice = random.randint(0, 3)
            for k in range(len(movementlist)):
                movementlist[k] = randint(0, 3)

        # also works on enemy movements using methods
        enemy = movement(movementchoice, enemy)
        enemy_rect_store = enemy_movement(enemy_rect_store, movementlist)

        # enemy laser movement using methods
        if reset != 1 and started == True:
            if start_timer > 120:
                fire = firerate(countdown, fire, enemy)
                fire_rect_list = firemove(countdown, fire_rect_list, enemy_rect_store)
                # blits all enemy lasers
                for blast in range(len(fire_rect_list)):
                    screen.blit(fire_image_list[blast], fire_rect_list[blast])
            start_timer += 1

        # laser set up
        for laser in lasers[:]:
            laser.y -= laser_speed
            if laser.y < 0:
                lasers.remove(laser)
            if laser.colliderect(enemy):
                enemyhealth -= 1
                if enemyhealth > 0:
                    damage.play()
                lasers.remove(laser)
            for i in range(len(enemy_rect_store)):
                if laser.colliderect(enemy_rect_store[i]):
                    hp_list[i] = hp_list[i] - 1
                    laser.y=-10
                    if hp_list[i] > 0:
                        damage.play()
                    if hp_list[i] <= 0:
                        death.play()
        # lowersHPs for the boss'''
        for laser in lasers[:]:
            if laser.colliderect(enemy):
                enemyhealth -= 1
                if enemyhealth > 0:
                    damage.play()
                lasers.remove(laser)


        # its draws/blits the laser don't fully know the difference it just works
        for laser in lasers:
            screen.blit(enemylaser, laser)

        # controls the timer for firing the bosses laser
        if countdown >= 120:
            countdown = 0

        # player death
        if (player_rect.collidelist(astroid_rect_store)) != -1 or (
        player_rect.colliderect(fire)) != False or player_rect.collidelist(
                fire_rect_list) != -1 or player_rect.collidelist(enemy_rect_store) != -1 or (
        player_rect.colliderect(enemy)) != False:
            counter = 0
            death.play()
            Dead = True

        # makes the game over screen
        if Dead == True:
            reset = 1
            start_timer = 0
            start = 0
            timetaken = seconds
            seconds_text = font.render(f"{seconds}", True, (255, 255, 255))
            astroid_rect_store = []
            astroid_surf_store = []
            astroid_move_store = []
            player_rect = player_surf.get_rect(center=(1000, 1000))
            for j in range(len(enemy_rect_store)):
                enemy_rect_store[j].x = 800
                enemy_rect_store[j].y = 800
                screen.blit(enemy_image_store[j], enemy_rect_store[j])
            enemy = pygame.Rect(800, 800, 50, 100)
            Game_Over = font2.render("You Died!! Game Over!!!", True, (255, 255, 255))
            time_taken_text = font2.render(f" Time Survived {timetaken} Seconds", True, (255, 255, 255))
            reset_text = font.render("Press R to Reset Game or Esc to Exit.", True, (255, 255, 255))
            screen.blit(Game_Over, (150, 300))
            screen.blit(time_taken_text, (140, 370))
            screen.blit(reset_text, (150, 450))

        # makes the game win screen and sets things up that I want to occur when the game win screen is not active
        if deathcount - enemyspawn == 0 and bossspawn == 0:
            reset = 1
            start_timer = 0
            start = 0
            astroid_rect_store = []
            astroid_surf_store = []
            astroid_move_store = []
            player_rect = player_surf.get_rect(center=(900, 900))
            if complete == 0:
                timetaken = seconds
                complete = 1
            Level_Complete = font2.render("Level Complete!!", True, (255, 255, 255))
            time_taken_text = font2.render(f" Time Taken {timetaken} Seconds", True, (255, 255, 255))
            reset_text = font.render("Press R to Reset Game or Esc to Exit.", True, (255, 255, 255))
            screen.blit(Level_Complete, (180, 300))
            screen.blit(time_taken_text, (170, 370))
            screen.blit(reset_text, (180, 450))
        else:
            if counter % 60 == 0 and Dead == False:
                seconds += 1
                seconds_text = font.render(f"{seconds}", True, (255, 255, 255))
            if counter % 300 == 0 and Dead == False:
                astroid_rect_store, astroid_surf_store, astroid_move_store = make_astroid(astroid_rect_store,
                                                                                          astroid_surf_store,
                                                                                          astroid_move_store)

        # sets up how the bosses health and what happens when it dies
        if enemyhealth > 0:
            enemysurf.fill((0, 255, 0))
        else:
            if bossspawn == 1:
                death.play()
            bossspawn = 0
            enemy = pygame.Rect(800, 800, 50, 100)

        # final blits and adding to counters or resetting important variables
        screen.blit(bosslaser, (fire.x, fire.y))
        screen.blit(boss_image, enemy)
        screen.blit(player_image, player_rect)
        timetillmove = timetillmove + 1
        countdown += 2
        deathcount = 0
        clock.tick(60)
        pygame.display.flip()


def instructions():
    pygame.display.set_caption("Instructions")
    font = pygame.font.SysFont(None, 34)
    font2 = pygame.font.SysFont(None, 64)
    font3 = pygame.font.SysFont(None, 37)
    time_text = font.render("Time:", True, (255, 255, 255))
    seconds_text = font.render(f"{seconds}", True, (255, 255, 255))
    highscore_text = font.render(f"{highscore} seconds", True, (255, 255, 255))
    reset_text = font.render("Press R to Reset Game.", True, (255, 255, 255))
    Game_Over = font2.render("Game Over!!!", True, (255, 255, 255))
    Level_Complete = font2.render("Level Complete!!", True, (255, 255, 255))
    time_taken_text = font2.render(f"{seconds} seconds", True, (255, 255, 255))


    while True:
        instructions_Mouse_POS = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))
        button = pygame.image.load('Butoon.png').convert_alpha()
        button = pygame.transform.scale(button, (600, 300))

        Game_Over = font3.render("First Objective: Survive; Don't hit the ships, lasers, or meteors.", True,
                                 (255, 255, 255))
        time_taken_text = font3.render("Second Objective: Destroy; Press the spacebar to fire lasers.", True,
                                       (255, 255, 255))
        Orders = font3.render("Kill everything in sight and remember meteors are unbreakable.", True, (255, 255, 255))
        Instructions = font3.render("Movement is 'w', 'a', 's', 'd'.", True, (255, 255, 255))
        screen.blit(Game_Over, (10, 330))
        screen.blit(time_taken_text, (10, 370))
        screen.blit(Orders, (10, 410))
        screen.blit(Instructions, (200, 450))


        instructionsBack = Button(image=button.convert_alpha(), pos=(150, 700),
                                  text_input="Back", font=get_font(37), base_color="black", hovering_color="white")
        instructionsBack.changeColor(instructions_Mouse_POS)
        instructionsBack.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if instructionsBack.checkForInput(instructions_Mouse_POS):
                    main_menu()
        clock.tick(60)
        pygame.display.update()


def main_menu():  # Main Menu Screen
    pygame.display.set_caption("Shoot or die!")

    while True:
        screen.blit(background, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        NameOfGame = get_font(100).render("Shoot or die!", True, "white")
        NameOfGameRect = NameOfGame.get_rect(center=(400, 100))
        button = pygame.image.load('Butoon.png').convert_alpha()
        button = pygame.transform.scale(button, (600, 300))

        play_button = Button(image=button.convert_alpha(), pos=(400, 250),
                             text_input="PLAY", font=get_font(37), base_color="black", hovering_color="black")
        instructions_button = Button(image=button.convert_alpha(), pos=(400, 450),
                                     text_input="INSTRUCTIONS", font=get_font(37), base_color="black",
                                     hovering_color="black")
        quit_button = Button(image=button.convert_alpha(), pos=(400, 700),
                             text_input="QUIT", font=get_font(37), base_color="black", hovering_color="black")
        screen.blit(NameOfGame, NameOfGameRect)
        for button in [play_button, instructions_button, quit_button]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(MENU_MOUSE_POS):
                    play()
                if instructions_button.checkForInput(MENU_MOUSE_POS):
                    instructions()
                if quit_button.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit

        pygame.display.update()


main_menu()
pygame.display.update()