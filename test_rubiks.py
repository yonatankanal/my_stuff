from rubiks_class import RubiksCube
import unittest

class TestRubiksCube(unittest.TestCase):

    def setUp(self):
        self.cube = RubiksCube()
    
    def test_og(self):
        self.cube.cube = ("".join(ele) for ele in self.cube.cube)
        self.assertEqual(
            self.cube.cube, 
            ["⬜⬜⬜⬜⬜⬜⬜⬜⬜","🟩🟩🟩🟩🟩🟩🟩🟩🟩","🟥🟥🟥🟥🟥🟥🟥🟥🟥","🟦🟦🟦🟦🟦🟦🟦🟦🟦","🟧🟧🟧🟧🟧🟧🟧🟧🟧","🟨🟨🟨🟨🟨🟨🟨🟨🟨"]
            )
        
    def test_u_move(self):
        self.cube.u_move()
        self.cube.cube = ("".join(ele) for ele in self.cube.cube)
        self.assertEqual(
            self.cube.cube,
            ["⬜⬜⬜⬜⬜⬜⬜⬜⬜","🟥🟥🟥🟩🟩🟩🟩🟩🟩","🟦🟦🟦🟥🟥🟥🟥🟥🟥","🟧🟧🟧🟦🟦🟦🟦🟦🟦","🟩🟩🟩🟧🟧🟧🟧🟧🟧","🟨🟨🟨🟨🟨🟨🟨🟨🟨"]
        )

    def test_d_move(self):
        self.cube.d_move()
        self.cube.cube = ("".join(ele) for ele in self.cube.cube)
        self.assertEqual(
            self.cube.cube,
            ["⬜⬜⬜⬜⬜⬜⬜⬜⬜","🟩🟩🟩🟩🟩🟩🟧🟧🟧","🟥🟥🟥🟥🟥🟥🟩🟩🟩","🟦🟦🟦🟦🟦🟦🟥🟥🟥","🟧🟧🟧🟧🟧🟧🟦🟦🟦","🟨🟨🟨🟨🟨🟨🟨🟨🟨"]
        )
        


if __name__ == '__main__':
    unittest.main()