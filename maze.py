from visuals import Cell
import time

class Maze():
    def __init__(self, num_rows, num_cols, window):
        self._x1 = 10
        self._y1 = 10
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = (1200 - 20) / (num_rows * 4)
        self.cell_size_y = (800 - 20) / (num_cols * 4)
        self._win = window
        self._cells = [] 
        self._create_cells()
        self._draw_cells()


    def _create_cells(self):
        for c in range(self.num_cols):
            row = ([
                Cell(
                    self._x1 + (self.cell_size_x * r), 
                    self._y1 + (self.cell_size_y * c), 
                    self._x1 + (self.cell_size_x * (r + 1)), 
                    self._y1 + (self.cell_size_y * (c + 1)),
                    self._win
                )
                for r in range(self.num_rows)
            ])
            self._cells.append(row)


    def _draw_cells(self):
        for col in self._cells:
            for cell in col:
                cell.draw()

        self._animate()
    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)
