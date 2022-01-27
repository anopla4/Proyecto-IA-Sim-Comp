from environment import Environment

class Agent:
    def __init__(self,action_list):
        self._ag_action_list=action_list
        self._ag_hist=[]
    
    # funcion Env:-> Action
    def agent_act(self,env:Environment):
        pass