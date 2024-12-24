from visuals import Cell
import time
import random

class Maze():
    def __init__(self, num_rows, num_cols, window, seed=None):
        self.initial_setup = True 
        self._x1 = 10
        self._y1 = 10
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = (1200) / (num_rows * 3.5)
        self.cell_size_y = (800) / (num_cols * 3.5)
        self._win = window
        self._cells = [] 
        self._create_cells()
        self._break_entrance_and_exit()
        self.seed = random.seed(seed)
        self.initial_setup = False


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
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
    
        self._cells[i][j].draw()
        if not(self.initial_setup):
            self._animate()


    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)


    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        start.has_left_wall = False 
        self._draw_cell(0, 0)
        end = self._cells[self.num_cols - 1][self.num_rows - 1]
        end.has_right_wall = False 

        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
        