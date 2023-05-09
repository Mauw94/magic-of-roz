from ast import List, Tuple
import heapq


class Pathfinding:
    def __init__(self, w, h):
        self.point_reached = False
        self.width = w
        self.height = h
        self.grid = {}

    def init_grid(self, w, h):
        for x in range(w):
            for y in range(h):
                self.grid[(x, y)] = 1

    def reset(self, w, h) -> None:
        self.grid = {}
        self.width = w
        self.height = h

    def find_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> set:
        distances = {node: float('inf') for node in self.grid}
        distances[start] = 0
        visited = set()
        queue = [(0, start)]

        while queue:
            cur_d, cur_node = queue.pop()
            if cur_node in visited:
                continue
            if cur_node == end:
                return visited
                # return distances[cur_node]
            if cur_d > distances[cur_node]:
                continue
            visited.add(cur_node)

            for n in self.__neighbours(cur_node[0], cur_node[1]):
                weight = self.grid[n]
                distance = cur_d + weight
                if distance < distances[n]:
                    distances[n] = distance
                    heapq.heappush(queue, (distance, n))

        return visited

    def find_next_coord(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[int]:
        # safe coord so no other entity can move to that coord
        # set can_find_new_coord to false until moved to that coord
        # when arrive at coord, find next coord
        # check saved moves, and/or find other coord
        # check up, down, left, right
        pass

    def __neighbours(self, x, y) -> List[int]:
        n = []
        n.append((x - 1, y))
        n.append((x + 1, y))
        n.append((x, y - 1))
        n.append((x, y + 1))

        return [x for x in n if x[0] >= 0 and x[0] < self.width and x[1] >= 0 and x[1] < self.height]
