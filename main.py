from tkinter import Tk, BOTH, Canvas


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y 


class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2 

    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self.point1.x, self.point1.y, 
            self.point2.x, self.point2.y, 
            fill=fill_colour, width=2
        )


class Cell():
    def __init__(self, x1, y1, x2, y2,  window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window

    def draw(self):
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")


class Window():
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._canvas = Canvas()
        self._canvas.pack()
        self._window_running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    
    def wait_for_close(self):
        self._window_running = True
        while self._window_running:
            self.redraw()

    def close(self):
        self._window_running = False


    def draw_line(self, line, fill_colour):
        line.draw(self._canvas, fill_colour)


win = Window(800, 600)
cell1 = Cell(1, 1, 11, 11, win)
cell2 = Cell(11, 1, 21, 11, win)
cell3 = Cell(21, 1, 31, 11, win)

cell1.draw()
cell2.draw()
cell3.draw()
win.wait_for_close()