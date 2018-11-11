import unittest
import Max


class TextMax(unittest.TestCase):

    def test_max(self):
        test_package_1 = [('word1', 10), ('word2', 20), ('word_max', 100)]
        test_package_2 = [('word1', 10), ('word_max', 100), ('word2', 20)]
        test_package_3 = []
        max_instance = Max.Max()
        self.assertEqual(('word_max', 100), max_instance.count_maximum(test_package_1))
        self.assertEqual(('word_max', 100), max_instance.count_maximum(test_package_2))
        self.assertEqual(('', -1), max_instance.count_maximum(test_package_3))
