from project.models.agent import Agent
from project.log_parser.log_line import LogLine


class PresenceLog(LogLine):
    def parse(self):
        self.linkCall()
        self.changeState()
        
    def linkCall(self):
        if self.getUcid():
            Agent(self.getUserId()).linkCall(self.getUcid())
    
    def changeState(self):
        if self.getUserId() and self.getAcdState():
            Agent(self.getUserId()).changeState(self.getAcdState())

    def getUserId(self):
        return self.search(r"UserId\{(.*?)\}")
        
    def getExtension(self):
        return self.search(r"Extension\{(.*?)\}")
        
    def getAcdState(self):
        state = self.search(r"Acd State\{(.*?)\}")
        if state==False:
            state = self.search(r"TpsSUserPresence::OnEvent. Rcvd Agent (ACDAVAIL)")
        return state
        
    def getLineState(self):
        return self.search(r"State\{(.*?)\}\}\]\}")
        
    def getUcid(self):
        return self.search(r"HandlingState:\{ContactId/RqC\{(.*?)\/")
