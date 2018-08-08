from module import TestModule
from collections import namedtuple

Query = namedtuple('Query', ('y', 'x'))


def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)
    ne = yield Query(y + 1, x + 1)
    e_ = yield Query(y + 0, x + 1)
    se = yield Query(y - 1, x + 1)
    s_ = yield Query(y - 1, x + 0)
    sw = yield Query(y - 1, x - 1)
    w_ = yield Query(y + 0, x - 1)
    nw = yield Query(y + 1, x - 1)
    
    neighbors_states = [n_, ne, e_, se, s_, sw, w_, nw]
 
