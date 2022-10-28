from unittest import TestCase
import func1, func2, func3, f4, f5, f6, f7, f8, f9, f10


class MyTests(TestCase):

    def test_func1(self):
        self.assertEqual(func1.day_of_week(5), 'No')
        self.assertEqual(func1.day_of_week(7), 'Yes')
        self.assertEqual(func1.day_of_week(9), 'Error')

    def test_func2(self):
        self.assertEqual(func2.sum_nums('523'), 10)
        self.assertEqual(func2.sum_nums('0.1234'), 10)

    def test_func3(self):
        self.assertEqual(func3.prod_num([2, 3, 4, 5, 6]), [12, 15, 16])

    def test_f4(self):
        self.assertEqual(f4.odd_ind([1, 35, 56, 4, 2, 7]), 46)

    def test_f5(self):
        self.assertEqual(f5.delete_word('Пайабвтон'), 'Пайтон')


class MyTests2(TestCase):

    def test_f6(self):
        self.assertEqual(f6.get_days(3), 31)

    def test_f7(self):
        self.assertEqual(f7.find_all('abcdabcaaa', 'a'), [0, 4, 7, 8, 9])

    def test_f8(self):
        self.assertTrue(f8.is_prime(17), True)
        self.assertFalse(f8.is_prime(18), True)

    def test_f9(self):
        self.assertTrue(f9.is_one_away('bike', 'hike'), True)
        self.assertFalse(f9.is_one_away('abcd', 'abpo'), True)

    def test_f10(self):
        self.assertTrue(f10.is_palindrome('А роза упала на лапу Азора.'), True)
        self.assertFalse(f10.is_palindrome('1223'), True)
