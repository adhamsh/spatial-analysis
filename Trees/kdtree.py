

class kDTreeNode():
    """
    Node for point k-D trees.
    """
    def __init__(self, point, left, right):
        self.point = point
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.point)

def kdcompare(r, p, depth):
    """
    Returns the branch of searching on a k-d tree
    Input
       r: root
       p: point
       depth : starting depth of search
    Output
       A value of -1 (left branch), or 1 (right)
    """
    k = len(p)
    dim = depth%k
    if p[dim] <= r.point[dim]:
        return -1
    else:
        return 1

def kdtree(points):
    """
    Creates a point k-D tree using a predefined order of points
    """
    root = kDTreeNode(point=points[0], left=None, right=None)
    for p in points[1:]:
        node = kDTreeNode(point=p, left=None, right=None)
        p0, lr = query_kdtree(root, p, 0, False)
        if p0 is None and lr is None:   # skip if duplicated
            continue
        if lr<0:
            p0.left = node
        else:
            p0.right = node
    return root

def kdtree_left(points, depth=0):
    """
    Creates a point k-d tree using the median point to split the data
    """
    if len(points)==0:
        return
    pivot = len(points)//2
    return kDTreeNode(points[pivot],
                      left=kdtree_left(points[:pivot], depth+1),
                      right=kdtree_left(points[pivot+1:], depth))


def kdtree2(points, depth = 0):
    """
    Creates a point k-d tree using the median point to split the data
    """
    if len(points)==0:
        return
    k = len(points[0])
    axis = depth % k
    points.sort(key=lambda p: p[axis])
    pivot = len(points)//2
    return kDTreeNode(points[pivot],
                      left=kdtree2(points[:pivot], depth+1),
                      right=kdtree2(points[pivot+1:], depth+1))

def query_kdtree(t, p, depth=0, is_find_only=True):
    """
    Input
      t:            a node of a point k-D tree
      p:            target point to be found in the tree
      depth:        the depth of node t (default 0)
      is_find_only: True to find if p exists, or False to find the parent node of p

    Output
      t:            the node that contains p or None (is_find_only is True)
                    the node that should be the parent node of p (is_find_only is False)
      lr:           None (is_find_only is True)
                    -1 -- indicating p be the left child node of t (is_find_only is False)
                    1  -- indicating p be the right child node of t (is_find_only is False)
    """
    if t is None:
        return None, None
    if t.point == p:
        if is_find_only:
            return t, None
        else:
            return None, None
    lr = kdcompare(t, p, depth)
    if lr<0:
        child = t.left
    else:
        child = t.right
    if is_find_only==False and child is None:
        return t, lr
    return query_kdtree(child, p, depth+1, is_find_only)

def left_right(tr, node_str):
    #answer=''
    if node_str == 'left' and tr.left:
        print('left YES')
            
    if node_str == 'right' and tr.right:
        print('right YES')
    else:
        print("none")
    
def depth(t):
    """
    Returns the depth of the tree
    """
    if t == None:
        return -1
    return max(depth(t.left)+1, depth(t.right)+1)

def tree_print(t):
    """
    This is adopted from the MIT OpenCourseWare at
    http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/readings/binary-search-trees/bst.py
    Now supports Python 3
    """
    def tree_print_helper(t):
        if t is None:
            return [], 0, 0
        # label = str(t.key)
        label = str(t)
        leftstr, leftpos, leftwidth = tree_print_helper(t.left)
        rightstr, rightpos, rightwidth = tree_print_helper(t.right)
        middle = max(rightpos+leftwidth - leftpos+1, len(label), 2)
        pos = leftpos + middle // 2
        width = leftpos + middle + rightwidth - rightpos
        while len(leftstr)<len(rightstr):
            leftstr.append(' '*leftwidth)
        while len(rightstr)<len(leftstr):
            rightstr.append(' '*rightwidth)
        if (middle-len(label))%2 == 1:
            label += '_'
        label = label.center(middle, '_')
        if label[0] == '_': label=' ' + label[1:]
        if label[-1] == '_': label = label[:-1]+' '
        lines = [' '*leftpos + label + ' '*(rightwidth-rightpos), ' '*leftpos + '/' + ' '*(middle-2) + '\\' + ' '*(rightwidth-rightpos)] + [leftline + ' '*(width-leftwidth-rightwidth) + rightline for leftline, rightline in zip(leftstr, rightstr)]
        return lines, pos, width
    print('\n'.join(tree_print_helper(t)[0]))

if __name__ == '__main__':
    import sys
    sys.path.append('../geom')
    from point import *



    data1 = [ (2,2), (0,5), (8,0), (9,8), (7,14), (13,12), (14,13) ]

    data1.append([50,50])
    data1.append([70,80])
    points = [Point(d[0], d[1]) for d in data1]
    p = points[0]
    t2 = kdtree(points)
    print(t2)
    tree_print(t2)


