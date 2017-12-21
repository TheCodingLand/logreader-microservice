class AgentEvent(object):
    def __init__(self, id):
        self.id = id
    
    def linkCall(self, ucid):
        print ("sending request for agent %s to link call %s" % (self.id, ucid))
        
    def changeState(self, state):
        print ("sending request for agent %s to change state to %s" % (self.id, state))
    