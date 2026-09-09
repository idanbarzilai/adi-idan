import pygame
import consts
import game_field


#initial placing of body
def body_initial_place():
    for i in range(0, consts.SOLDIER_BODY_ROWS):
        for j in range(consts.SOLDIER_COLS):

            game_field.game_field_matrix[i][j] = consts.BODY_SQUARE
            consts.BODY_PLACE.append([i,j])
            #אם לא תעבוד הרשימה של כל הגוף אז להוסיף פה הוספה


#initial placing of legs
def legs_initial_place():
    row = consts.SOLDIER_BODY_ROWS
    for j in range(consts.SOLDIER_COLS):
        game_field.game_field_matrix[row][j] = consts.LEGS_SQUARE
        consts.LEGS_PLACE.append([row,j])


def create_soldier():
    body_initial_place()
    legs_initial_place()
    consts.SOLDIER_PLACE = consts.BODY_PLACE + consts.LEGS_PLACE
    print(consts.BODY_PLACE)
    print(consts.LEGS_PLACE)
    print(consts.SOLDIER_PLACE)

    x = game_field.get_x(consts.SOLDIER_PLACE[0][1])
    y = game_field.get_y(consts.SOLDIER_PLACE[0][0])
    return {
        "x": x,
        "y": y,
        "w": game_field.get_w(x , consts.SOLDIER_COLS),
        "h": game_field.get_h(y , consts.SOLDIER_ROWS)
    }

#checking if soldier steps on mine
def is_soldier_on_mine():
    for item in consts.LEGS_PLACE:
        if item == consts.MINE_SQUARE:
            return True
    return False

#checking if soldier grab flag
def is_soldier_on_flag():
    for item in consts.BODY_SQUARE:
        if item == consts.FLAG_SQUARE:
            return True
    return False


#לבדוק אם הרשימהמ של כל המקומות במטריצה של כל המשחק ואם כן אז להזיז את השחקנים
def is_in_field(place):
    return place in game_field.game_field_matrix
#place of body
def movement_type(event):
        d_up_down = 0
        d_left_right = 0
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
        if new_r >= consts.BOARD_ROWS or new_c >= consts.BOARD_COLS:
            in_mat = False
            break
    if in_mat:
        for item in consts.SOLDIER_PLACE:
            item[0] += dR
            item[1] += dC










