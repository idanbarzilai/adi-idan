import pygame
import soldier
import consts
import game_field


def create_soldier_screen():
    soldier1 = pygame.image.load("soldier.png")
    s = soldier.create_soldier()
    sized_soldier = pygame.transform.scale(s1, (s["w"] ,s["h"]))

    soldier_box = pygame.surface((s["w"], s["h"]),)
    #fill
    soldier_box.blit(sized_soldier,(0,0))
    return soldier_box

def drow_soldier(soldier1):
    #צריך גם להכניס את התזוזה?

    screen.blit(soldier1,)






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