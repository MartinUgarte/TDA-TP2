import unittest

from solucion_optima import empaquetamiento_optimo

class TestEncapsulamientoBacktracking(unittest.TestCase):

    def test_no_hay_objetos(self):
        T = []
        resultado = []
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))

    def test_un_objeto_menor_que_envase(self):
        T = [0.2]
        resultado = [[0.2]]
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))

    def test_un_objeto_igual_que_envase(self):
        T = [1]
        resultado = [[1]]
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))

    def test_dos_objetos_un_envase(self):
        T = [0.6, 0.2]
        resultado = [[0.6, 0.2]]
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))

    def test_dos_objetos_entran_justo_un_envase(self):
        T = [0.6, 0.4]
        resultado = [[0.6, 0.4]]
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))
    
    def test_dos_objetos_dos_envases(self):
        T = [0.6, 0.8]
        resultado = [[0.6],[0.8]]
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))
    
    def test_tres_objetos_dos_envases(self):
        T = [0.5, 0.6, 0.4]
        resultado = [[0.5, 0.4], [0.6]]
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))

    def test_tres_objetos_entran_justo_dos_envases(self):
        T = [0.7, 0.6, 0.3]
        resultado = [[0.7, 0.3], [0.6]]
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))

    def test_tres_objetos_tres_envases(self):
        T = [0.9, 0.4, 0.8]
        resultado = [[0.9], [0.4], [0.8]]
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))

    def test_cuatro_objetos_dos_envases(self):
        T = [0.4, 0.8, 0.6, 0.2]
        resultado = [[0.4, 0.6], [0.8, 0.2]]
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))
    
    def test_caso_ejemplo(self):
        T = [0.4, 0.8, 0.5, 0.1, 0.7, 0.6, 0.1, 0.4, 0.2, 0.2]
        resultado = [[0.4, 0.5, 0.1], [0.7, 0.1, 0.2], [0.2, 0.8], [0.6, 0.4]]
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))

    def test_caso_ejemplo_env3(self):
        T = [0.085, 0.006, 0.008, 0.024, 0.106, 0.357, 0.001, 0.915, 0.643, 0.255, 0.513, 0.039, 0.048]
        resultado = [[], [], []]
        self.assertEqual(len(empaquetamiento_optimo(T)[0]), len(resultado))

if __name__ == "__main__":
    unittest.main()