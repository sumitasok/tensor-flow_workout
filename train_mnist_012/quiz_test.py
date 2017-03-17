import unittest
import numpy as np

from quiz import softmax

class TestQuizMethods(unittest.TestCase):

    def test_softmax(self):
        # status = softmax([1.0, 2.0, 3.0]) == [ 0.09003057, 0.24472847, 0.66524096]
        np.testing.assert_allclose(softmax([1.0, 2.0, 3.0]), [ 0.09003057, 0.24472847, 0.66524096])

if __name__ == '__main__':
    unittest.main()