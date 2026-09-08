import consts
import game_field

#changing img to the right size
def body_initial_place():
    for i in range(0, consts.SOLDIER_BODY_ROWS):
        for j in range(consts.SOLDIER_COLS):
            l = [i,j]
            game_field.game_field_matrix[i][j] = consts.BODY_SQUARE
            consts.BODY_PLACE.append(l)
            l=[]


def legs_initial_place():
    for i in range(0, consts.SOLDIER_BODY_ROWS):
        for j in range(consts.SOLDIER_COLS):
            l = [i, j]
            game_field.game_field_matrix[i][j] = consts.LEGS_SQUARE
            consts.LEGS_PLACE.append(l)
            l = []


def create_soldier(center_x, center_y, color):
    body_initial_place()
    legs_initial_place()






