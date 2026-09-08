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


def


