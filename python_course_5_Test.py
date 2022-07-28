# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-26
    Author: John Huang
'''

from math import pi, sqrt
import unittest
from python_course_5 import Circle, Square, Rectangle, Triangle

# ======== Geometry Test =========

class GeometryTest(unittest.TestCase):

    def testSquare(self): 
        s = Square(side=5) 
        self.assertEqual( s.Area() , 25 )
        self.assertEqual( s.Perimeter(), 20 ) 

    def testRectangle(self):
        r = Rectangle(length=3, width=7)
        self.assertEqual( r.Area(), 21 )
        self.assertEqual( r.Perimeter(), 20 )

    def testCircle(self): 
        c = Circle(radius=3)
        self.assertEqual( c.Area(), 9*pi)
        self.assertEqual( c.Perimeter(), 6*pi)

    def testEquiTriangle(self): 
        t = Triangle(side_A=10, side_B=10, side_C=10)
        self.assertEqual( t.Area(), 25 * sqrt(3))
        self.assertEqual( t.Perimeter(), 30)

    def testRightTriangle(self): 
        t = Triangle(side_A=5, side_B=4, side_C=3)
        self.assertEqual( t.Area(), 6)
        self.assertEqual( t.Perimeter(), 12) 

if __name__ == '__main__': 
    unittest.main(verbosity=4)
