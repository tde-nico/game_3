import pygame
from scripts.entity import Entity
from scripts.phisics import *
from scripts.ground import *
from scripts.controller_handler import *
from scripts.load_skins import import_skin



L = 1360
H = 750

pygame.init()
pygame.display.set_caption("Game Name")
screen = pygame.display.set_mode((L,H),pygame.SCALED + pygame.RESIZABLE)
clock = pygame.time.Clock()



maps = list_maps()
grounds, ground_datas = generate_ground_from_file(screen, maps[0])

controllers = get_controllers()
controllers_life = []
for controller in range(len(controllers)):
    controllers_life.append(True)
players = []
standard_x = 100
#colors = [(0,0,200),(200,200,0),(200,0,0),(0,200,0)]

for player in range(len(controllers)):
    #players.append(Entity(screen, standard_x + player*100, 200, 40, 60, colors[player], speed=6, interaction='player')) #colors[player]
    players.append(Entity(screen, standard_x + player*100, 200, 40, 60, speed=6, interaction='player'))
    players[player].right = import_skin('skins\\player_test_' + str(player) + '\\right')
    players[player].left = import_skin('skins\\player_test_' + str(player) + '\\left')
    players[player].stand = pygame.image.load('skins\\player_test_' + str(player) + '\\standing.png')
    
bullets = []
entities = [players, bullets]







def redraw():
    screen.fill((0,0,0))

    for entity_type in entities:
        for entity in entity_type:
            entity.draw()
    
    for ground in grounds:
        ground.draw()
    
    pygame.display.update()
    


run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    controller_number_fix = 0
    all_keys = []
    for controller in range(len(controllers)):
        if not controllers_life[controller]:
            controller_number_fix += 1
            continue
        keys = [0,0,0,0,0,0,0]
        axes, buttons = get_controller_events(controllers[controller - controller_number_fix])
        
        if axes[0] <= -.2: keys[0] = -axes[0]
        elif buttons[13]: keys[0] = 1
        if axes[0] >= .2: keys[1] = axes[0]
        elif buttons[14]: keys[1] = 1
        if axes[1] <= -.2: entities[0][controller - controller_number_fix].direction[1] = axes[1]
        elif buttons[11]: entities[0][controller - controller_number_fix].direction[1] = -1
        #print(controller)
        if axes[1] >= .2: keys[3] = axes[1]
        elif buttons[12]: keys[3] = 1

        keys[2] = buttons[0]
        keys[4] = buttons[1]
        keys[5] = buttons[2]

        all_keys.append(keys)
            
    
        
    for player in range(len(entities[0])):
        entities[0][player].move(all_keys[player])
        #print(player, entities[0][player].direction)
        
    for bullet in entities[1]:
        bullet.move()

    for entity_type in entities:
        for entity in entity_type:
            entity.y += 7

    for player in range(len(entities[0])):
        if all_keys[player][5] and entities[0][player].left_bullets > 0:
            shot, shot_data = entities[0][player].shoot()
            entities[1].append(shot)
            #entities_data+=str(shot_data[0])+' '+str(shot_data[1])+' '+str(shot_data[2][0])+' '+str(shot_data[2][1])+' '+str(shot_data[2][2])+' '+str(shot_data[3][0])+' '+str(shot_data[3][1])+' '+str(shot_data[3][2])+'\n'
           

    for entity_type in entities:
        for entity in entity_type:
            for ground in grounds:
                collision = collision_fix(entity, ground)
                if collision[1]:
                    entity.ground = True
                if collision[0]:
                    entity.wall = True
                    

    for player in range(len(entities[0])):
        for bullet in range(len(entities[1])):
            collision = check_collision(entities[1][bullet], entities[0][player])
            #print(collision)
            if (collision[0] or collision[1]) and not entities[0][player].hit:
                entities[0][player].hit = True
                entities[1][bullet].y = 10000
                print('hit')
                #print(entities[0][player].health)


    for player in range(len(entities[0])):
        print(entities[0][player].health)
        #if entities[0][entity_number].health <= 0: entities[0][entity_number].lifes -= 1
        if entities[0][player].y > H or entities[0][player].x > L or entities[0][player].x < -entities[0][player].height or entities[0][player].hit:
            entities[0][player].health -= 1
            #print(entities[0][player].health)
            print('damage')
            entities[0][player].hit = False
            if entities[0][player].health <= 0:
                entities[0][player] = 0
                controllers_life[player] = False
            elif not entities[0][player].in_respawn:
                entities[0][player].respawn()
                #print(entities[0][entity_number].health)
                

    for entity_number in range(len(entities[1])):
        if entities[1][entity_number].y > H or entities[1][entity_number].x > L or entities[1][entity_number].x < -entities[1][entity_number].height:
            entities[1][entity_number].lifes = 0

    for entity_type in range(len(entities)):
        for entity in entities[entity_type]:
            if not entity:
                entities[entity_type].remove(entity)
            elif entity.lifes <= 0:
                entities[entity_type].remove(entity)
                if not entity_type:
                    controllers_life[entity_type] = False

            
    redraw()

pygame.quit()

    
