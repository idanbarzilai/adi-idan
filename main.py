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
        event_handler()

        pygame.display.update()
    pygame.quit()

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            dr, dc = 0, 0
            if event.key == pygame.K_SPACE:
                #משנה את הסטטוס שדארק
                game_state["screen_status"] = "dark"
            if event.key == pygame.K_UP:
                dr = -1
            elif event.key == pygame.K_DOWN:
                dr = 1
            elif event.key == pygame.K_LEFT:
                dc = -1
            elif event.key == pygame.K_RIGHT:
                dc = 1
        if dr != 0 or dc != 0:

            player_r, player_c, pts, mine = move_player(dungeon, player_r, player_c, dr, dc)
            score += pts
            if mine:
                lives -= 1
                print("BOOM! Hit a mine. Lives left:", lives)

if __name__ == '__main__':
    main()