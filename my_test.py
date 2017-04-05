import unittest
from matrix import Matrix

class test1(unittest.TestCase):
	def setUp(self):
		self.t1 = [[1,1,1],[2,2,2],[3,4,5,6,7,8,9]]

	def test_init(self):
		m1 = Matrix(self.t1)
		self.assertEqual(self.t1[0],m1.rows[0])
		self.assertEqual(self.t1[1],m1.rows[1])
		self.assertEqual(self.t1[2],m1.rows[2])

class test2(unittest.TestCase):
	def setUp(self):
		self.t1 = [[1,1,1],[2,2,2]]
		self.tr = [[2,2,2],[4,4,4]]

	def test_init(self):
		m1 = Matrix(self.t1)
		m2 = Matrix(self.t1)
		m3 = m1 + m2
		self.assertEqual(self.tr,m3.rows)

if __name__ == '__main__':
	unittest.main()
