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






