import unittest
import ScoreCounter


class TestScoreCounter(unittest.TestCase):

    def test_result(self):
        test_word_1 = 'test'
        test_word_2 = '2323'
        test_word_3 = ''
        self.assertEqual(4, ScoreCounter.ScoreCounter.result(test_word_1))
        self.assertEqual(0, ScoreCounter.ScoreCounter.result(test_word_2))
        self.assertEqual(0, ScoreCounter.ScoreCounter.result(test_word_3))

    def test_count_for_all(self):
        test_package_1 = ['word1', 'woooord2']
        scorecounter_instance = ScoreCounter.ScoreCounter(test_package_1)
        expected_result = [('word1', 8), ('woooord2', 11)]
        self.assertEqual(expected_result, scorecounter_instance.count_for_all())
