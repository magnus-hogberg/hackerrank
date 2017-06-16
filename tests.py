import unittest
from breaking_best_and_worst_records.solution import get_record
from knightl.knightl import knightl
from equal import solution


class TestSolution(unittest.TestCase):
    # def test1(self):
    #     result = solution.solve(5, [1, 2, 1, 3, 2], 3, 2)
    #     self.assertEqual(result, 2)
    #
    # def test2(self):
    #     result = solution.solve(6, [1, 1, 1, 1, 1, 1], 3, 2)
    #     self.assertEqual(result, 0)
    #
    # def test3(self):
    #     result = solution.solve(1, [4], 4, 1)
    #     self.assertEqual(result, 1)
    #
    # def test4(self):
    #     result = solution.solve(19, [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1], 18, 7)
    #     self.assertEqual(result, 3)

    def knightl_test1(self):
        result = knightl(5)
        self.assertEqual(result, [[4, 4, 2, 8], [4, 2, 4, 4], [2, 4, -1, -1], [8, 4, -1, 1]])

    def test1(self):
        result = get_record([10, 5, 20, 20, 4, 5, 2, 25, 1])
        self.assertEqual(result, [2, 4])

    def test2(self):
        result = get_record([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
        self.assertEqual(result, [4, 0])

    def test_equal_1(self):
        result = solution.search([2, 2, 3, 7])
        self.assertEqual(result, 2)

    def test_equal_2(self):
        result = solution.search([53, 361, 188, 665, 786, 898, 447, 562, 272, 123, 229, 629, 670, 848, 994, 54, 822, 46,
                                  208, 17, 449, 302, 466,
                                  832, 931, 778, 156, 39, 31, 777, 749, 436, 138, 289, 453, 276, 539, 901, 839, 811, 24,
                                  420, 440, 46, 269, 786,
                                  101, 443, 832, 661, 460, 281, 964, 278, 465, 247, 408, 622, 638, 440, 751, 739, 876,
                                  889, 380, 330, 517, 919,
                                  583, 356, 83, 959, 129, 875, 5, 750, 662, 106, 193, 494, 120, 653, 128, 84, 283, 593,
                                  683, 44, 567, 321, 484,
                                  318, 412, 712, 559, 792, 394, 77, 711, 977, 785, 146, 936, 914, 22, 942, 664, 36, 400,
                                  857])
        self.assertEqual(result, 10605)

    def test_equal_3(self):
        result = solution.search([1, 5, 5])
        self.assertEqual(result, 3)
