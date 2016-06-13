import os
import unittest
from cmdlinetool import test


def run():
    path = os.path.dirname(test.__file__)
    suite = unittest.TestLoader().discover(path)
    unittest.TextTestRunner(verbosity=2).run(suite)
