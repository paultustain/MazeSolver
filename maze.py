from visuals import Cell
import time
import random

class Maze():
    def __init__(self, num_rows, num_cols, window, seed=None):
        self.initial_setup = True 
        self._x1 = 10
        self._y1 = 10
        self._num_rows = num_rows
        self._num_cols = num_cols
        self.cell_size_x = (1200) / (num_rows * 3.5)
        self.cell_size_y = (800) / (num_cols * 3.5)
        self._win = window
        self._cells = [] 
        self.seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

        self._reset_cells_visited()
        self.initial_setup = False


    def _create_cells(self):
        for c in range(self._num_cols):
            row = ([
                Cell(
                    self._x1 + (self.cell_size_x * r), 
                    self._y1 + (self.cell_size_y * c), 
                    self._x1 + (self.cell_size_x * (r + 1)), 
                    self._y1 + (self.cell_size_y * (c + 1)),
                    self._win
                )
                for r in range(self._num_rows)
            ])
            self._cells.append(row)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
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
        end = self._cells[self._num_cols - 1][self._num_rows - 1]
        end.has_right_wall = False 

        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
        

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))

            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))

            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))

            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            next_cell_x, next_cell_y = random.choice(next_index_list)

            if next_cell_x == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_cell_x == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_cell_y == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_cell_y == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_cell_x, next_cell_y)
    

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._cells[i][j].visited = False

    
    def solve(self):
        return self._solve_r(self, 0, 0)

    def _make_move(self, i, j, x, y):
        print("make move")
        self._cells[i][j].draw_move(self._cells[i + x][j + y])
        if self._solve_r(i + x, j + y):
            return True
        self._cells[i][j].draw_move(self._cells[i + x][j + y], True)
        return False
        
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True 

        print(i, j, 
            "top: ", self._cells[i][j].has_top_wall, 
            "bottom: ", self._cells[i][j].has_bottom_wall,
            "left: ", self._cells[i][j].has_left_wall,
            "right: ", self._cells[i][j].has_right_wall
        )

        if i == self._num_cols - 1 and j == self._num_rows - 1: 
            return True 
        
        for direction_x, direction_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if direction_x == -1 and i > 0:
                if (
                    not self._cells[i][j].has_left_wall 
                    and not self._cells[i - 1][j].visited
                ):
                    if self._make_move(i, j, direction_x, direction_y):
                        return True

            if direction_x == 1 and i < self._num_cols - 1:
                if (
                    (not self._cells[i][j].has_right_wall) 
                    and (not self._cells[i + 1][j].visited)
                ):
                    if self._make_move(i, j, direction_x, direction_y):
                        return True

            if direction_y == -1 and j > 0:
                if (
                    not self._cells[i][j].has_top_wall 
                    and not self._cells[i][j - 1].visited
                ):
                    if self._make_move(i, j, direction_x, direction_y):
                        return True                    
            
            if direction_y == 1 and j < self._num_rows - 1:
                if (
                    not self._cells[i][j].has_bottom_wall 
                    and not self._cells[i][j + 1].visited
                ):
                    if self._make_move(i, j, direction_x, direction_y):
                        return True

        return False
 