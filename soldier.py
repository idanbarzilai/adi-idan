import pygame
import consts
import game_field


#initial placing of body
def body_initial_place():
    for i in range(0, consts.SOLDIER_BODY_ROWS):
        for j in range(consts.SOLDIER_COLS):
            l = [i,j]
            game_field.game_field_matrix[i][j] = consts.BODY_SQUARE
            consts.BODY_PLACE.append(l)
            l=[]

#initial placing of legs
def legs_initial_place():
    for i in range(0, consts.SOLDIER_FEET_ROWS):
        for j in range(consts.SOLDIER_COLS):
            l = [i, j]
            game_field.game_field_matrix[i][j] = consts.LEGS_SQUARE
            consts.LEGS_PLACE.append(l)
            l = []

def create_soldier():
    body_initial_place()
    legs_initial_place()

    return {
        "x": game_field.get_x(consts.BODY_PLACE),
        "y": consts.SOLDIER_COLS*consts.CELL_SIZE
        "w":
    }

#checking if soldier steps on mine
def is_soldier_on_mine():
    for item in consts.LEGS_PLACE:
        if game_field.game_field_matrix[item] == consts.MINE_SQUARE:
            return True
    return False

#checking if soldier grab flag
def is_soldier_on_flag():
    for item in consts.BODY_SQUARE:
        if game_field.game_field_matrix[item] == consts.FLAG_SQUARE:
            return True
    return False


#לבדוק אם הרשימהמ של כל המקומות במטריצה של כל המשחק ואם כן אז להזיז את השחקנים
def is_in_field(place):
    return place in game_field.game_field_matrix
#place of body
def movement_type(event):
        if event.type == pygame.KEYDOWN:
            d_up_down = 0
            d_left_right = 0
            if event.key == pygame.K_UP:
                d_up_down = -1
                d_left_right = 0
            elif event.key == pygame.K_DOWN:
                d_up_down = 1
                d_left_right = 0
            elif event.key == pygame.K_LEFT:
                d_up_down = 0
                d_left_right = -1
            elif event.key == pygame.K_RIGHT:
                d_up_down = 0
                d_left_right = 1
        return [d_up_down,d_left_right]

def movement(event):
    dR = movement_type(event)[0]
    dC = movement_type(event)[1]

    consts.SOLDIER_PLACE = consts.BODY_PLACE + consts.LEGS_PLACE

    in_mat = True
    for item in consts.SOLDIER_PLACE:
        new_r = item[0] + dR
        new_c = item[1] + dC
        if [new_r][new_c] not in game_field.game_field_matrix:
            in_mat = False
            break
    if in_mat:
        for item in consts.SOLDIER_PLACE:
            item[0] += dR
            item[1] += dC










