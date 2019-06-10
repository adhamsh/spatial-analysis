 #The point import is a class for points in Cartesian coordinate systems
from point import *

def normalize(corner, quadmap, width, height):
    old_height = len(quadmap)
    old_width = len(quadmap[0])
    if old_height == height and old_width == width:
        return quadmap
    else:
        blank_width = width - old_width
        if corner == 'nw':
            new = [' '*width for i in range(height - old_height)]
            for line in quadmap:
                new.append(' '*blank_width + line)
        elif corner == 'ne':
            new = [' '*width for i in range(height - old_height)]
            for line in quadmap:
                new.append(line + ' '*blank_width)
        elif corner == 'sw':
            new = []
            for line in quadmap:
                new.append(' '*blank_width + line)
            for i in range(height - old_height):
                new.append(' '*width)
        elif corner == 'se':
            new = []
            for line in quadmap:
                new.append(line + ' '*blank_width)
            for i in range(height - old_height):
                new.append(' '*width)
        return new

class PQuadTreeNode():
    def __init__(self,point,nw=None,ne=None,se=None,sw=None):
        self.point = point
        self.quadrants = {'nw':nw, 'ne':ne, 'se':se, 'sw':sw}

    def __repr__(self):
        return '\n'.join(self.get_map())

    def is_leaf(self):
        return all(q == None for q in self.quadrants.values())

    def get_depth(self):
        if self.is_leaf():
            return 1
        else:
            return 1 + max(q.get_depth() if q else 0 for q in self.quadrants.values())

    def get_map(self):
        if self.is_leaf():
            return [str(self.point)]
        else:
            subquadmaps = {
                sqn:sq.get_map() if sq else ['.']
                for sqn, sq
                in self.quadrants.items()
            }
            subheight = max(len(map) for map in subquadmaps.values())
            subwidth = max(len(mapline) for map in subquadmaps.values() for mapline in map)
            subquadmapsnorm = {
                sqn:normalize(sqn, sq, subwidth, subheight)
                for sqn, sq
                in subquadmaps.items()
            }
            map = []
            for n in range(subheight):
                map.append(subquadmapsnorm['nw'][n] + '|' + subquadmapsnorm['ne'][n])
            map.append('-' * (subwidth-num_length-1) + str(self.point) + '-' * (subwidth-num_length-1))
            for n in range(subheight):
                map.append(subquadmapsnorm['sw'][n] + '|' + subquadmapsnorm['se'][n])
            return map

def search_pqtree(q, p, is_find_only=True):
    if q is None:
        return
    if q.point == p:
        if is_find_only:
            return q
        else:
            return
    dx,dy = 0,0
    if p.x >= q.point.x:
        dx = 1
    if p.y >= q.point.y:
        dy = 1
    qnum = dx+dy*2
    child = [q.quadrants['sw'], q.quadrants['se'], q.quadrants['nw'], q.quadrants['ne']][qnum]
    if child is None and not is_find_only:
        return q
    return search_pqtree(child, p, is_find_only)

def insert_pqtree(q, p):
    n = search_pqtree(q, p, False)
    node = PQuadTreeNode(point=p)
    if p.x < n.point.x and p.y < n.point.y:
        n.quadrants['sw'] = node
    elif p.x < n.point.x and p.y >= n.point.y:
        n.quadrants['nw'] = node
    elif p.x >= n.point.x and p.y < n.point.y:
        n.quadrants['se'] = node
    else:
        n.quadrants['ne'] = node

def pointquadtree(data):
    root = PQuadTreeNode(point = data[0])
    for p in data[1:]:
        insert_pqtree(root, p)
    return root

num_length = 2
num_fmt = '%' + str(num_length) + 'd'
#Test
data1 = [ (2,2), (0,5), (8,0), (9,8), (7,14), (13,12), (14,13) ]

points = [Point(d[0], d[1]) for d in data1]
q = pointquadtree(points)
print(q)

