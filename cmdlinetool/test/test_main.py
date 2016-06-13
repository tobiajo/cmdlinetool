import os
import unittest
from .. import test


def run():
    path = os.path.dirname(test.__file__)
    suite = unittest.TestLoader().discover(path)
    result = unittest.TextTestRunner(verbosity=2, failfast=False).run(suite)
    if not result.wasSuccessful():
        return 1
