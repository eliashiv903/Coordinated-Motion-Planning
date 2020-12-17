
# A data structure for queue used in BFS
import Point


class queueNode:
    def __init__(self, pt: Point, dist: int, path: []):
        self.pt = pt  # The cordinates of the cell
        self.dist = dist  # Cell's distance from the source
        self.path = path

    def __repr__(self):
        return str(self.path)

    def __str__(self):
        return str(self.path)
