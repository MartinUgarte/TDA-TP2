import unittest
from encapsulamiento import encapsulamiento

class TestEncapsulamientoBacktracking(unittest.TestCase):

    def test_caso_ejemplo(self):
        T = [0.4, 0.8, 0.5, 0.1, 0.7, 0.6, 0.1, 0.4, 0.2, 0.2]
        resultado = [[0.4, 0.5, 0.1], [0.7, 0.1, 0.2], [0.8, 0.2], [0.6, 0.4]]
        self.assertEqual(encapsulamiento(T), resultado)

if __name__ == "__main__":
    unittest.main()