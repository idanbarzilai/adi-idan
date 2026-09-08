import consts

#changing img to the right size
def body_initial_place():
    consts.BODY_PLACE[0] = [0,0]
    consts.BODY_PLACE[1] = [0,1]
    consts.BODY_PLACE[2] = [1,0]
    consts.BODY_PLACE[3] = [1,1]
    consts.BODY_PLACE[4] = [2, 0]
    consts.BODY_PLACE[5] = [2, 1]

def legs_initial_place():
    consts.LEGS_PLACE[0] = [3,0]
    consts.LEGS_PLACE[1] = [3,1]

def make_square_empty(lst):
#creating soldier
def create_soldier(center_x, center_y, color):
    body_initial_place()

    return {"place": consts.SOLDIER_START_PLACE,
            "center_x": center_x,
            "center_y": center_y,
            "radius": consts.BUBBLE_RADIUS}

def body_place():

def legs_place():


