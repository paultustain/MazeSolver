from visuals import Window
from maze import Maze

def main():
    win = Window(1200, 800)
    # cell1 = Cell(10, 50, 100, 100,  win)
    # cell2 = Cell(11, 1, 21, 11, win)
    # cell3 = Cell(21, 1, 31, 11, win)
    # cell1.draw()
    # cell2.draw()
    # cell3.draw()
    # cell1.draw_move(cell2)
    # cell2.draw_move(cell3, True)
    maze = Maze(3, 3, win)
    win.wait_for_close()

main()