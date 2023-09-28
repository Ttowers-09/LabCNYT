import unittest
import numpy as np
import base as mt

class TestCplxOperations(unittest.TestCase):


    def test_probabilidadposition (self):
        v1 = np.array ([complex(2,1), complex(-1,2), complex(0,1), complex(1,0),complex(3,-1),complex(2,0),complex(0,-2),complex(-2,1),complex(1,-3),complex(0,-1)])
        p = 7
        probabilidad = mt.probabilidad_position(v1, p)
        self.assertAlmostEqual(probabilidad, 0.1086956521739130)

        v1 = np.array([complex(-3, -1), complex(0, -2), complex(0, 1), complex(2, 0)])
        p = 2
        probabilidad = mt.probabilidad_position(v1, p)
        self.assertAlmostEqual(probabilidad, 0.052 , places= 2)



    def test_prueba(self):
        v1 = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        v2 = np.array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        expected = np.array([complex(0, 0)])
        probabilidad = mt.probabilidad_transito(v1, v2)
        np.testing.assert_almost_equal(probabilidad, expected)

        v1 = np.array ([complex(2,1), complex(-1,2), complex(0,1), complex(1,0),complex(3,-1),complex(2,0),complex(0,-2),complex(-2,1),complex(1,-3),complex(0,-1)])
        v2 = np.array ([complex(-1,-4), complex(2,-3), complex(-7,6), complex(-1,1),complex(-5,-3),complex(5,0),complex(5,8),complex(4,-4),complex(8,-7),complex(2,-7)])
        expected = np.array([complex(-0.020556626417313734, -0.1301919673096537)])
        probabilidad = mt.probabilidad_transito(v1, v2)
        np.testing.assert_almost_equal(probabilidad, expected)



if __name__ == '__main__':
    unittest.main()
