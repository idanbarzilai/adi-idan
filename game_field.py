
game_field_matrix = []

def create_row_game_field ():
    row = []
    for index in range(const.row)#אורך שורה מהקונסט
        row.append(const.empty) #משתנה של ריק
    return row.copy()

#יוצר את הרשימה של הלוח משחק
def create_game_field():
    global game_field_matrix

    for row in range(const.orhrahnv): #אורך המטריצה