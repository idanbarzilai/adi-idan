import random
from random import randrange

import consts

game_field_matrix = []

#יוצר רשימה של שורה אחת ריקה
def create_row_game_field ():
    row = []
    for index in range(consts.BOARD_COLS):#אורך שורה מהקונסט
        row.append(consts.NO_MINE_SQUARE) #משתנה של ריק
    return row.copy()

#יוצר את הרשימה של הלוח משחק
def create_game_field():
    global game_field_matrix

    for row in range(consts.BOARD_ROWS): #אורך המטריצה
        game_field_matrix.append(create_row_game_field()) #מוסיף שורה ריקה לרשימה


def create_flag ():

    top_row = consts.BOARD_ROWS - consts.FLAG_ROWS #משתנה ששומר את הגובה של הדגל במטריצה
    top_col = consts.BOARD_COLS - consts.FLAG_COLS #משתנה ששומר את רוכב הדגל במטריצה

    for row in range(len(game_field_matrix) - 1 , -1 , -1 ):

        if top_row <= (row + 1): #בודק אם הגעתי עברתי את המיקום האחרון
            break

        for col in range(len(game_field_matrix[row]) - 1 , -1 , -1 ):
            if top_col <= (col + 1): #בודק אם הגעתי ועברתי את המיקום האחרון בשורה
                break
            game_field_matrix[row][col] = consts.FLAG_SQUARE #משתנה של דגל

#יוצר מוקש במיקום רנדומאלי
def create_mine():
    row = random.randrange(0, consts.BOARD_ROWS)
    col = random.randrange(0, (consts.BOARD_COLS - 2))

    while (all_reday_mine(row,col)):
        row = random.randrange(0, consts.BOARD_ROWS)
        col = random.randrange(0, (consts.BOARD_COLS - 2))

    return ({ #מילון


    })


    #להוסיף שנוצר מילון ששומר את הערכים של שורה תור פעולת x ופעולת y



#פעולה שבודקת אם כבר יש מוקש בערכים שקבלנו
def all_reday_mine(row,col):

    all_reday = False
    for i in range(3):
        if not (game_field_matrix[row][(col + i)] == consts.EMPTY_SQUARE):
            all_reday = True

    return all_reday




def multiple_mine():

    #לולאה שעוברת לפי מספר המוקשים שמבוקש
    #יוצרת מוקש
    #מוסיפה אותו לרשימת מוקשים

def add_mines_to_game_field():


    #לולאה שעוברת על כל הרשימה
    MINES_LIST
        for i in range(3):
            game_field_matrix[row][(col + i)] = consts.MINE_SQUARE




def get_x(col): # מקבל את המיקום בשורה ומחזיר את המיקום x שלו במסך
    return (col * consts.CELL_SIZE)


def get_y(row):#מקבל באיזה שורה זה נמצא ומחזיר את מיקום y שלו במסך
    return (row * consts.CELL_SIZE)


def get_w(x , num_col):#מקבל את מיקום הx של האובייקט ומחזיר את הרוחב שלו (ערך הx בפינה הימנית)
    return (x * num_col)


def get_h(y, num_row):# מקבל את המיקום y  של האובייקט ומחזיר את הגובה שלו, בערך של y בקצה התחתון של האובייקט
    return (y * num_row)

