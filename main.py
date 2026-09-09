import pygame
import consts
import screen
import soldier

game_state = {
    "state": consts.RUNNING_STATE,
    "original_screen": True,
    "dark_screen": False
}

def main():

    pygame.init()
    running = True
    while running:
        screen.draw_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
          ##  if event.type == pygame.Enter
            soldier.movement(event)
            if soldier.is_soldier_on_flag() or soldier.is_soldier_on_mine():
                running = False


        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()



