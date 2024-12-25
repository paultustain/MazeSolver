from visuals import Window
from maze import Maze

def main():
    win = Window(1200, 800)
    maze = Maze(12, 16, win, 10)

    maze._solve_r(0, 0)
    win.wait_for_close()

main()