
from math import sqrt

class Point:
    '''A class for points in Cartesian coordinate systems.'''
    def __init__(self, x=None, y=None, key=None):
        self.x = x
        self.y = y
        self.key = key
    def __getitem__(self, i):
        if i==0: return self.x
        if i==1: return self.y
        return None
    def __len__(self):
        return 2
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x==other.x and self.y==other.y
        return NotImplemented
    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
    def __lt__(self, other):
        if isinstance(other, Point):
            if self.x<other.x:
                return True
            elif self.x==other.x and self.y<other.y:
                return True
            return False
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Point):
            if self.x>other.x:
                return True
            elif self.x==other.x and self.y>other.y:
                return True
            return False
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, Point):
            if self > other or self == other:
                return True
            else:
                return False
            return False
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Point):
            if self < other or self == other:
                return True
            else:
                return False
            return False
        return NotImplemented
    def isvalid(self):
        if not isinstance(self.x, (int, float)) \
                or not isinstance(self.y, (int, float)):
            return False
        return True
    def __str__(self):
        '''NaP: Not a point'''
        if not self.isvalid():
            return 'NaP'
        if isinstance(self.x, (int)):
            fmtstr = '({0}, '
        else:
            fmtstr = '({0:.1f}, '
        if isinstance(self.y, (int)):
            fmtstr += '{1})'
        else:
            fmtstr += '{1:.1f})'
        return fmtstr.format(self.x, self.y)
    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)
    def distance(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
