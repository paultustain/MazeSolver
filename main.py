from visuals import Window
from maze import Maze

def main():
    win = Window(1200, 800)
    maze = Maze(25, 35, win)
    win.wait_for_close()

main()