import unittest
import WordFinder

class TestWordFinder(unittest.TestCase):

    def test_search_a_word(self):
        testing_package = [('word1', 1), ('word2', 2), ('word3', 3), ('word4', 5)]
        wordfinder_instance_1 = WordFinder.WordFinder(testing_package, 2)
        wordfinder_instance_2 = WordFinder.WordFinder(testing_package, 5)
        wordfinder_instance_3 = WordFinder.WordFinder(testing_package, 4)
        self.assertEqual(wordfinder_instance_1.search_a_word(), ('word2', 1))       # '1' is not a score, it's an index!
        self.assertEqual(wordfinder_instance_2.search_a_word(), ('word4', 3))       # so as '3'
        self.assertEqual(wordfinder_instance_3.search_a_word(), None)

    def test_find_all_matching_words(self):
        testing_package = [('word1', 1), ('word2', 2), ('word3', 3), ('word4', 5), ('word5', 5), ('word6', 5), ('word7', 6)]
        wordfinder_instance_2 = WordFinder.WordFinder(testing_package, 5)
        expected_list = ['word4', 'word5', 'word6']
        self.assertEqual(expected_list, wordfinder_instance_2.find_all_matching_words())
