

def get_surface(obj):
    return (obj.x,obj.y),(obj.x+obj.width,obj.y),(obj.x+obj.width,obj.y+obj.height),(obj.x,obj.y+obj.height)


def check_collision(entity_1, entity_2):
    s1 = get_surface(entity_1)
    s2 = get_surface(entity_2)
    
    x_condition = ((s1[0][0]>s2[0][0] and s1[0][0]<s2[1][0]),(s1[1][0]>s2[0][0] and s1[1][0]<s2[1][0]))
    y_condition = ((s1[0][1]>s2[0][1] and s1[0][1]<s2[2][1]),(s1[2][1]>s2[0][1] and s1[2][1]<s2[2][1]))
    
    if (x_condition[0] or x_condition[1]) and (y_condition[0] or y_condition[1]):
        collision = (not (x_condition[0] and x_condition[1]), not (y_condition[0] and y_condition[1]))
    else:
        collision = (False, False)

    return collision


def collision_fix(entity_1, entity_2):
    collision = check_collision(entity_1, entity_2)
    fixed_collision = [False, False]
    if collision[0] and collision[1]:
        if entity_2.y < entity_1.y + entity_1.height and entity_2.y > entity_1.y:
            entity_1.y = entity_2.y - entity_1.height
            fixed_collision[1] = True
        if entity_2.y + entity_2.height > entity_1.y and entity_2.y < entity_1.y and entity_2.x < entity_1.x + entity_1.width and entity_2.x > entity_1.x:
            entity_1.x = entity_2.x - entity_1.width
            fixed_collision[0] = True
        elif entity_2.y + entity_2.height > entity_1.y and entity_2.y < entity_1.y and entity_2.x + entity_2.width > entity_1.x and entity_2.x < entity_1.x:
            entity_1.x = entity_2.x + entity_2.width
            fixed_collision[0] = True
            
    elif collision[0]:
        if entity_2.x < entity_1.x + entity_1.width and entity_2.x > entity_1.x:
            entity_1.x = entity_2.x - entity_1.width
        if entity_2.x + entity_2.width > entity_1.x and entity_2.x < entity_1.x:
            entity_1.x = entity_2.x + entity_2.width
        fixed_collision[0] = True
            
    elif collision[1]:
        if entity_2.y < entity_1.y + entity_1.height and entity_2.y > entity_1.y:
            entity_1.y = entity_2.y - entity_1.height
            fixed_collision[1] = True
        if entity_2.y + entity_2.height > entity_1.y and entity_2.y < entity_1.y:
            entity_1.y = entity_2.y + entity_2.height
    
    return fixed_collision
    
