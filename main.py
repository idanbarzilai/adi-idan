import pygame
import consts
import soldier

state = {
    "state": consts.RUNNING_STATE
}

def main():
    running = True
    while running:
        # screen.fill(COLOR_PANEL)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            soldier.movement(event)
            if soldier.is_soldier_on_flag() or soldier.is_soldier_on_mine():
                running = False

