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

def empty_place_given(lst):
    for item in lst:
        game_field.game_field_matrix[item[0]][item[1]] = consts.EMPTY_SQUARE

#לעבור על הלולאה להפוך את המקומות הקודמים לריקים ואת החדשים לגוף ורגליים , לא צריך לבדוק תקינות כי היא נבדקה כבר
def movement(dr,dc):
    empty_place_given(consts.SOLDIER_PLACE)
    counter1=0
    counter2=0
    for item in consts.BODY_PLACE:
        if (item[0] + dr) < 0 or (item[0]+dr)>=consts.BOARD_ROWS or (item[1] + dc) < 0 or (item[1]+dc)>=consts.BOARD_COLS:
            counter1+=1
    for item in consts.LEGS_PLACE:
        if item[0] + dr < consts.BOARD_ROWS or item[0]+dr>=consts.BOARD_ROWS or item[1] + dc < consts.BOARD_COLS or item[1]+dc>=consts.BOARD_COLS:
            counter2+=1
    if counter1== 0 or counter2== 0:
       for item in consts.BODY_PLACE:
           item[0] += dr
           item[1] += dc
           game_field.game_field_matrix[item[0]][item[1]] = consts.BODY_SQUARE
       for item in consts.LEGS_PLACE:
           item[0] += dr
           item[1] += dc
           game_field.game_field_matrix[item[0]][item[1]] = consts.LEGS_PLACE
    consts.SOLDIER_PLACE = consts.BODY_PLACE + consts.LEGS_PLACE
    print(consts.SOLDIER_PLACE)





