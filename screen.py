import random

import pygame
import soldier
import consts
import game_field

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))



def draw_soldier(soldier_creation, png = consts.SOLDIER):
    soldier_image = pygame.image.load(png)
    sized_soldier = pygame.transform.scale(soldier_image, (soldier_creation["w"] * 2, soldier_creation["h"]))
    screen.blit(sized_soldier,(soldier_creation["x"],soldier_creation["y"]))


def draw_flag():
    flag_image = pygame.image.load(consts.FLAG_IMG)
    sized_flag = pygame.transform.scale(flag_image,(game_field.get_x(consts.FLAG_COLS),game_field.get_y(consts.FLAG_ROWS)))
    screen.blit(sized_flag,(game_field.get_x(consts.FLAG_COL), game_field.get_y(consts.FLAG_ROW)))

def draw_mines():
    mine_image = pygame.image.load(consts.MINE_IMG)
    sized_mine = pygame.transform.scale(mine_image,(game_field.get_x(consts.MINE_COLS),game_field.get_y(consts.MINE_ROW)))
    for mine in consts.MINES_LIST:
        screen.blit(sized_mine,(mine["mine_x"],mine["mine_y"]))


def draw_grid_black():
    screen.fill(consts.BACKGROUND_DARK_SCREEN)
    '''
        for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            pygame.draw.rect(screen, consts.BACKGROUND_DARK_SCREEN, i * consts.CELL_SIZE, j=consts.CELL_SIZE,
                             width=1)
    '''


def draw_bushs():
    bushs_image = pygame.image.load(consts.GRASS_IMG)
    sized_bushs = pygame.transform.scale(bushs_image,(60,60))
    for bushs in range(20):
        screen.blit(sized_bushs, (game_field.get_x(random.randrange(0, (consts.BOARD_COLS - 2))), (game_field.get_y(random.randrange(0, consts.BOARD_ROWS)))))

def draw_welcom():
    pass

def draw_win():
    pass
def draw_loss():
    pass


def draw_game(game_state):
    if game_state["screen_status"] == 'light' :
        screen.fill(consts.BACKGROUND_SCREEN)
        draw_soldier(game_state['soldier'])
        draw_flag()
        draw_bushs()

        draw_welcom()

        if(game_state["state"] == 3):
            draw_win()

        elif(game_state["state"] == 2):
            draw_loss()





    elif game_state["screen_status"] == "dark":
        draw_grid_black()
        draw_soldier(game_state['soldier'], consts.SOLDIER_NIGHT_IMG)
        draw_flag()
        draw_mines()
        pygame.time.delay(10000000)
        game_state["screen_status"] = "light"


    pygame.display.flip()




'''

def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_arrow(game_state["rotated_arrow"])

    if game_state["is_bubble_fired"]:
        draw_bubble(game_state["bullet_bubble"])

    BubblesGrid.draw()
    draw_border()
    draw_turns(game_state["turns_left_to_add_row"])
    Stack.draw()

    if len(game_state["bubbles_popping"]):
        BubblesGrid.animate_bubbles_pop(game_state["bubbles_popping"])
        draw_bubbles_popping(game_state["bubbles_popping"])

    elif game_state["state"] == consts.LOSE_STATE:
        draw_lose_message()

    elif game_state["state"] == consts.WIN_STATE:
        draw_win_message()

    pygame.display.flip()




def draw_bubble(bubble):
        pygame.draw.circle(screen, bubble["color"],
                           center=(bubble["center_x"], bubble["center_y"]),
                           radius=bubble["radius"])


def create_arrow(arrow_img):
    arrow = pygame.image.load(arrow_img)
    sized_arrow = pygame.transform.scale(arrow, (
        consts.ARROW_WIDTH, consts.ARROW_HEIGHT))

    # Create a box to put the arrow in, so that the rotation will be around
    # it's bottom (the box's center)
    arrow_box = pygame.Surface(
            (consts.ARROW_WIDTH, consts.ARROW_HEIGHT * 2), )
    arrow_box.fill(consts.BACKGROUND_COLOR)
    arrow_box.blit(sized_arrow, (0, 0))

    return arrow_box


def draw_arrow(arrow):
    rotated_arrow_rect = arrow.get_rect(
            center=(consts.ARROW_MIDBOTTOM_X, consts.ARROW_MIDBOTTOM_Y))
    screen.blit(arrow, rotated_arrow_rect)

'''