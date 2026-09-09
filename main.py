import pygame
import consts
import soldier

game_state = {
    "state": consts.RUNNING_STATE,
    "original_screen": True,
    "dark_screen": False
}

def main():
    running = True
    while running:
        # screen.fill(COLOR_PANEL)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
          ##  if event.type == pygame.Enter
            soldier.movement(event)
            if soldier.is_soldier_on_flag() or soldier.is_soldier_on_mine():
                running = False






#screen
screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_game(game_state):
    if game_state["original_screen"]:
       screen.fill(consts.BACKGROUND_SCREEN)
    elif game_state["dark_screen"]:
        screen.fill(consts.BACKGROUND_DARK_SCREEN)
        for i in range(consts.BOARD_ROWS):
            for j in range(consts.BOARD_COLS):
                pygame.draw.rect(screen, consts.BACKGROUND_DARK_SCREEN, i * consts.CELL_SIZE, j = consts.CELL_SIZE, width=1)

    if len(game_state["bubbles_popping"]):
        BubblesGrid.animate_bubbles_pop(game_state["bubbles_popping"])
        draw_bubbles_popping(game_state["bubbles_popping"])

    elif game_state["state"] == consts.LOSE_STATE:
        draw_lose_message()

    elif game_state["state"] == consts.WIN_STATE:
        draw_win_message()

    pygame.display.flip()

