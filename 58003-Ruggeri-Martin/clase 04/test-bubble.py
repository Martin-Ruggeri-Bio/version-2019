import unittest
from bubble_sort import bubble
class TestBubble (unittest.TestCase):
    def test_bubble (self):
        lista=[4,1,3,6,5]
        ordenada=bubble(lista)
        self.assertEqual(ordenada,[1,3,4,5,6])
if __name__=='__main__':
    unittest.main()