#consts for screen
BACKGROUND_SCREEN = (143, 188, 143)
MESSAGE_TEXT = "Welcome to The Flag game.\nHave Fun!"
EXPLOTION_IMG = "explotion.png"
FLAG_IMG = "flag.png"
GRASS_IMG = "grass.png"
GUARD_IMG = "guard.png"
INJURY_IMG = "injury.png"
MINE_IMG = "mine.png"
SNAKE_IMG = "snake.png"
SOLDIER = "soldier.png"
SOLDIER_NIGHT_IMG = "soldier_night.png"
TELEPORT_IMG = "teleport.png"

#const for screen field
BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE

#consts for soldier
SOLDIER_ROWS = 4
SOLDIER_COLS = 2
SOLDIER_BODY_ROWS = 3 # the upper part
SOLDIER_FEET_ROWS = 1 # the lower part
SOLDIER_START_PLACE = (0,0)

#consts for flag
FLAG_ROWS = 3
FLAG_COLS = 4
FLAG_ROW = BOARD_ROWS - FLAG_ROWS
FLAG_COL = BOARD_COLS - FLAG_COLS

#consts for mines
MINES_COUNT = 20
MINE_ROW = 1
MINE_COLS = 3

#const for square
NO_MINE_SQUARE = "EMPTY"

#consts for status:
RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3

