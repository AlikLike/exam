import tested_progr
import unittest
import sys



class TestArr(unittest.TestCase):

    def test_basic(self):
        cases = (1,3,5)

        results = (1,6,120)

        for a, r in zip(cases, results):
            with self.subTest(case=a):
                b_r = tested_progr.main(a)
                self.assertTrue((b_r==r),msg="test_basic: a = " + str(a) + ", b_r = " + str(b_r) + ", r = " + str(r))

def sort_test_suite():
    suite = unittest.TestSuite()

    suite.addTest(TestArr('test_basic'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    test_suite = sort_test_suite()
    runner.run(test_suite)
