import unittest

from core.pathfinding.pathfinder import Pathfinding


class PathfinderTests(unittest.TestCase):

    def test_path_finding(self):
        self.path_finder.init_grid(100, 100)
        v = self.path_finder.find_path((0, 0), (10, 10))

        print(len(v))
        # for x in v:
        #     print(x)

    def setUp(self):
        pass
        self.path_finder = Pathfinding(100, 100)
