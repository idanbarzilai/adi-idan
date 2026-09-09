import pygame
import consts
import screen
import soldier
import game_field

game_state = {
    "state": consts.RUNNING_STATE,
    "screen_status": 'light',
    "soldier" : None
}

def main():
    game_field.create_game_field()  # יוצר את הגיים פילד
    game_state["soldier"] = soldier.create_soldier()

    pygame.init()
    running = True
    while running:
        screen.draw_game(game_state)

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









