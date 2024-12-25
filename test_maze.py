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

    def test_cells_visited(self):
        num_cols = 12
        num_rows = 16 
        m1 = Maze(num_rows, num_cols, None, 10)

        self.assertEqual( 
            [[cell.visited for cell in row] for row in m1._cells], 
            [[False for _ in range(num_rows)] for _  in range(num_cols)]
        )

if __name__ == "__main__":
    unittest.main()