from visuals import Point, Line, Cell, Window

def main():
    win = Window(800, 600)
    cell1 = Cell(1, 1, 11, 11, win)
    cell2 = Cell(11, 1, 21, 11, win)
    cell3 = Cell(21, 1, 31, 11, win)

    cell1.draw()
    cell2.draw()
    cell3.draw()
    win.wait_for_close()

main()