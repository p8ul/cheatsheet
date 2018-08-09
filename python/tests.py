# Skeleton
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

class TestXxx(unittest.TestCase):

    def setUp(self):
        ...

    def tearDown(self):
        ...

    def test_yyy_description1(self):
        ...
        
    def test_yyy_description2(self):
        ...
# Basic tests
self.assertTrue(1 + 2 == 3)
self.assertFalse(1 + 2 == 4)
self.assertEqual(actual, expected)
self.assertNotEqual(actual, not_expected)
self.assertIn('b', ['a', 'b', 'c'])

assetIs(a,b) a is b
assetIsNot(a,b) a is not b
assertIsNone(x) x is not
assertIn(a,b) a in b
assettNotIn(a,b) a not in b
assertIsInstance(a,b) issintance(a,b)
assertNotIsInstance(a,b) no issinstance(a,b)

assertRaises(exc, fun, args, *kwds) fun(*args, **kwds) raises exc
assertRaisesRegexp(exc,r,fun,args,*kwds) round(a-b, 7) == 0
assertAlmostEqual(a,b)
assertNotAlmostEqual(a,b)
assertGreater(a,b)
assertGreaterEqual(a,b) a >= b
assertLess(a,b) a < b
assertLessEqual(a,b) a <= b
assertItemsEqual(a,b)
assertDictContainsSubset(a,b) all the key/value pairs in an existing in b
