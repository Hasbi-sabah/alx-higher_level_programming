import models.base as b
import unittest
class TestBase(unittest.TestCase):
    def test_module_doc(self):
        self.assertIsNotNone(b.__doc__)
        self.assertGreater(len(b.__doc__), 0)
    def test_class_doc(self):
        self.assertIsNotNone(b.Base.__doc__)
        self.assertGreater(len(b.Base.__doc__), 0)
    def test_method_doc(self):
        self.assertIsNotNone(b.Base.__init__.__doc__)
        self.assertGreater(len(b.Base.__init__.__doc__), 0)
    def setUp(self):
        b.Base._Base__nb_objects = 0
    def test_base_id_incr(self):
        self.assertEqual(b.Base().id, 1)
        self.assertEqual(b.Base().id, 2)
        self.assertEqual(b.Base().id, 3)
        self.assertEqual(b.Base().id, 4)
        self.assertEqual(b.Base().id, 5)
    def test_base_id_input(self):
        self.assertEqual(b.Base(89).id, 89)
        self.assertEqual(b.Base(-89).id, -89)
        self.assertEqual(b.Base(0).id, 0)
    def test_base_id_mix(self):
        self.assertEqual(b.Base(89).id, 89)
        self.assertEqual(b.Base().id, 1)
        self.assertEqual(b.Base(0).id, 0)
        self.assertEqual(b.Base().id, 2)
        self.assertEqual(b.Base().id, 3)
        self.assertEqual(b.Base(-1).id, -1)
        self.assertEqual(b.Base(4).id, 4)
if __name__ == '__main__':
    unittest.main()
