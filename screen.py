import pygame
import soldier
import consts
import game_field

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))



def drow_soldier(soldier):

    soldier_image = pygame.image.load("soldier.png")
    sized_soldier = pygame.transform.scale(soldier_image, (soldier["w"], soldier["h"]))
    screen.blit(sized_soldier,(soldier["x"],soldier["y"])


def draw_game(game_state):
    if game_state["original_screen"]:
        screen.fill(consts.BACKGROUND_SCREEN)
    elif game_state["dark_screen"]:
        screen.fill(consts.BACKGROUND_DARK_SCREEN)
        for i in range(consts.BOARD_ROWS):
            for j in range(consts.BOARD_COLS):
                pygame.draw.rect(screen, consts.BACKGROUND_DARK_SCREEN, i * consts.CELL_SIZE, j=consts.CELL_SIZE,
                                    width=1)

    pygame.display.flip()




'''
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