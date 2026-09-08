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
    for i in range(0, consts.SOLDIER_BODY_ROWS):
        for j in range(consts.SOLDIER_COLS):
            l = [i, j]
            game_field.game_field_matrix[i][j] = consts.LEGS_SQUARE
            consts.LEGS_PLACE.append(l)
            l = []

def create_soldier():
    body_initial_place()
    legs_initial_place()

    return {
        "x": consts.SOLDIER_ROWS*consts.CELL_SIZE,
        "y": consts.SOLDIER_COLS*consts.CELL_SIZE
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

#place of body






