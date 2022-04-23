import pygame
from scripts.standard_functions import invoke


class Entity():
    def __init__(self, screen, x, y, width, height, color=0, speed=0, direction=[0,0], ground=True, interaction='ground'):

        self.screen = screen
        
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction
        self.interaction = interaction
        
        
        self.jump = False
        self.max_jumps = 2
        self.jumps_left = self.max_jumps
        self.jumping_value = 25
        self.jump_instance = 0
        self.jump_delay = True

        self.ground = ground

        self.max_dashes = 1
        self.left_dashes = self.max_dashes

        self.left_bullets = 1
        
        self.wall = False
        self.wall_delay = True

        self.health = 2
        self.lifes = 1
        self.in_respawn = False
        self.hit = False

        self.walk_count = 0


    def draw(self):
        if self.color:
            pygame.draw.rect(self.screen, self.color,(self.x,self.y,self.width,self.height))
        else:
            if self.walk_count >= 27:
                self.walk_count = 0
            if self.direction[0] < -.3:
                self.screen.blit(self.left[self.walk_count//3], (self.x,self.y))
                #self.walk_count += 1
            elif self.direction[0] > .3:
                self.screen.blit(self.right[self.walk_count//3], (self.x,self.y))
                #self.walk_count +=1
            else:
                self.screen.blit(self.stand, (self.x, self.y))
                
            

    def move(self, keys=[0,0,0,0]):

        if self.interaction == 'player':
            if keys[0]:
                self.x -= self.speed * keys[0]
                self.direction[0] = -keys[0]
                self.walk_count += 1
            if keys[1]:
                self.x += self.speed * keys[1]
                self.direction[0] = keys[1]
                self.walk_count += 1
            if not keys[0] and not keys[1]: self.direction[0] = 0
            if keys[2]:
                if self.jumps_left > 0 and self.jump_delay:
                    self.jump = True
                    self.jumps_left -= 1
                    self.jump_delay = False
                    self.jump_instance = 0
                    invoke(self, 'jump_delay', True, .2)
                    self.ground = False
                
                self.direction[1] = -keys[2]
            if keys[3]:
                self.y += self.speed
                self.direction[1] = keys[3]

            if self.wall and self.wall_delay:
                self.wall = False
                self.wall_delay = False
                if self.jumps_left < self.max_jumps:
                    self.jumps_left += 1
                
            if self.jump:
                self.y += -self.jumping_value + self.jump_instance
                self.jump_instance += 1
                if self.jumping_value-self.jump_instance <= 4:
                    self.jump = False
                    self.jump_instance = 0
            elif self.ground:
                self.jumps_left = self.max_jumps
                self.wall_delay = True
                         
            if keys[4] and self.left_dashes > 0:
                self.dash()
                
        elif self.interaction == 'bullet':
            if self.wall:
                self.direction[0] *= -1
                self.wall = False
            
            self.x += self.speed * self.direction[0]
            self.y -= 3
            

            if self.direction[1] < 0 and self.jump_delay and self.jumps_left > 0 and self.left_dashes:
                self.jump = True
                self.jumps_left -= 1
                self.left_dashes = 0
                self.jumping_value = 18
                
            
            if self.jump:
                self.ground = False
                self.jump_delay = False
                self.y += -self.jumping_value + self.jump_instance
                self.jump_instance += 1.5
                if self.jumping_value-self.jump_instance <= 4:
                    self.jump = False
                    self.jump_delay = True
                    self.jump_instance = 0
            elif self.ground:
                if self.jumps_left > 0:
                    self.jumps_left = 0
                    self.jump = True
                    self.jumping_value = 16
                elif not self.jump:
                    self.lifes = 0
                
                
		          

    def dash(self):
        self.speed *= 5
        self.left_dashes -=1
        invoke(self, 'speed', self.speed/5, .1)
        invoke(self, 'left_dashes', self.max_dashes, 1)


    def shoot(self):
        self.left_bullets -=1
        invoke(self, 'left_bullets', 1, 1)
        if self.direction == [0,0]:
            orientation = [0, -1]
        else:
            orientation = [self.direction[0],self.direction[1]]
        x = self.x + self.width/2 + orientation[0] * self.width/2
        y = self.y + orientation[1] * self.height/2 
        color = (150,50,50)
        measures = (15,10)
        return Entity(self.screen, x, y, measures[0], measures[1], color, speed=8, ground=False, direction=orientation, interaction='bullet'), (x, y, measures, color)


    def respawn(self):
        self.x = 750
        self.y = -5000
        self.in_respawn = True
        invoke(self, 'in_respawn', False, 2)
        invoke(self, 'x', 750, .5)
        invoke(self, 'x', 700, 1)
        invoke(self, 'x', 700, 1.5)
        invoke(self, 'x', 750, 2)
        invoke(self, 'y', 100, 2)
        




        

        

    
