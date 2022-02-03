from .node import Node
import math
from random import randint

class UCT(object):
    def __init__(self, c : float = math.sqrt(2)):
        self.c = c

    @staticmethod
    def uct_value(node : Node):
        if node.visit_count == 0:
            return 1e9
        return node.utility_score/node.visit_count + math.sqrt(math.log10(node.parent.visit_count)/node.visit_count)
    
    @staticmethod
    def find_best_utc(candidates:list[Node]):
        best = -1e9
        best_candidates = []
        for child in candidates:
            utc_v = UCT.uct_value(child)
            if utc_v > best:
                best_candidates = [child]
                best = utc_v
            elif utc_v == best:
                best_candidates.append(child)
        b = best_candidates[randint(0, len(best_candidates)-1)]    
        return b