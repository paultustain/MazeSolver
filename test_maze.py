import unittest 
from maze import Maze 

class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(num_rows, num_cols, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_single(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(num_rows, num_cols, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_large(self):
        num_cols = 120
        num_rows = 100
        m1 = Maze(num_rows, num_cols, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()