from typing import Dict


class Node(object):
    def __init__(self, value:str, parent = None, creation_time = 0, id = -1):
        self._value:str = value
        self._arrival_state:Dict[str,float] = {}
        self._final_state:Dict[str,float] = {}
        self._parent:Node = parent
        self._children:list[Node] = []
        self._created_time = creation_time
        self._id = id
        self._visit_count:int = 0
        self._utility_score:float = 0
        self._probability_value:float = 0

    @property
    def name(self)->str:
        return f"{self._id} {self.value}:{self._created_time}"

    @property
    def value(self)->str:
        return self._value

    @property
    def parent(self):
        return self._parent

    @property
    def utility_score(self):
        return self._utility_score
    
    @utility_score.setter
    def utility_score(self,utility_score:float):
        self._utility_score=utility_score

    @property
    def probability_value(self):
        return self._probability_value
    
    @probability_value.setter
    def probability_value(self,probability_value:float):
        self._probability_value=probability_value

    @property
    def visit_count(self):
        return self._visit_count
    
    @visit_count.setter
    def visit_count(self,visit_count:float):
        self._visit_count=visit_count

    @property
    def arrival_state(self):
        return self._arrival_state

    def update_arrival_state(self, new_arrival_state:Dict[str,float])->None:
        for p, v in new_arrival_state.items():
            if self._arrival_state.get(p) == None:
                self._arrival_state[p] = 0
            self._arrival_state[p]+=v

    def get_average_arrival_state(self)->Dict[str,float]:
        avg_state = {}
        for p,v in self._arrival_state.items():
            avg_state[p] = v/self.visit_count
        return avg_state

    @property
    def final_state(self):
        return self._final_state

    def update_final_state(self, new_final_state:Dict[str,float])->None:
        for p, v in new_final_state.items():
            if self._final_state.get(p) == None:
                self._final_state[p] = 0
            self._final_state[p]+=v

    def get_average_final_state(self)->Dict[str,float]:
        avg_state = {}
        for p,v in self._final_state.items():
            avg_state[p] = v/self.visit_count
        return avg_state

    @property
    def intervention(self):
        return self._value

    @property
    def created_time(self):
        return self._created_time

    def empty(self)->bool:
        return self._value == ""

    def __str__(self) -> str:
        return f"""
        Value: {self.value}
        Visit_count: {self.visit_count}
        Utility_score: {self.utility_score}
        Childrens_count: {len(self._children)}
        """