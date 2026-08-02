import unittest
import cmath

from solver import Solver

class testSolver(unittest.TestCase):
    
    def test_rg58(self):
        rg58 = Solver("Copper", "Polyethylene", "Dunno", 0.000405, 0.001475, 1, 1, 1000000000)
        rg58.solve()
        self.assertTrue(abs(rg58.z0.real-50)<5)
        self.assertTrue(abs(rg58.z0.imag-0)<5)
        
    def test_rg59(self):
        rg59 = Solver("Copper", "Polyethylene", "Dunno", 0.00029, 0.00185, 1, 1, 1000000000)
        rg59.solve()
        self.assertTrue(abs(rg59.z0.real-75)<5)
        self.assertTrue(abs(rg59.z0.imag-0)<5)

    def test_rg8(self):
        rg8 = Solver("Copper", "Polyethylene", "Dunno", 0.001085, 0.00362, 1, 1, 1000000000)
        rg8.solve()
        self.assertTrue(abs(rg8.z0.real-50)<5)
        self.assertTrue(abs(rg8.z0.imag-0)<5)

    def test_rg142(self):
        rg142 = Solver("Copper", "Polyethylene", "Dunno", 0.00047, 0.00151, 1, 1, 1000000000)
        rg142.solve()
        self.assertTrue(abs(rg142.z0.real-50)<5)
        self.assertTrue(abs(rg142.z0.imag-0)<5)

    def test_airlossless(self):
        airlossless = Solver("Copper", "Air", "Dunno", 0.0005, 0.0015, 1, 1, 1000000000)
        airlossless.solve()
        self.assertTrue(abs(airlossless.z0.imag) < 5)
        

if __name__ == '__main__':
    unittest.main()
