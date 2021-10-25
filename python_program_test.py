import unittest
import python_program


class python_testing(unittest.TestCase):
    def test_power_function(self):
        ans=python_program.cal_square(9)
        self.assertEqual(ans, 81)
    
    def test_sum_function(self):
        ans=python_program.cal_sum_of_n(100)
        self.assertEqual(ans, 5050)



unittest.main()