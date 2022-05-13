
class SwitchNode(object):
    def __init__(self):
        self.link_to = []
        self.path = {}
        self.store = []
        self.switch_table = {}

    def add_link(self,x):
        self.link_to.append(x)
        if(x not in self.path.keys()):
            self.path[x] = 1
    
    def add_store(self,x):
        self.store.append(x)

    def check_table(self,x):
        if(x in self.switch_table):
            return 1
        else:
            return 0
    

    