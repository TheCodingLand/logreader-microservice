from project.models.call_event import CallEvent
from project.log_parser.log_line import LogLine


class TelephonyLog(LogLine):
    def __init__(self, line):
        super(TelephonyLog, self).__init__(line)
        self.date = self.getDate()
        
    
    def parse(self):
        self.check_createNew()
        self.getDetails()

        
    def check_createNew(self):
        if self.getNewCallUcid():
            CallEvent.add(self.getDate(),self.getNewCallUcid())
    
    def getDetails(self):
        if "UpdateRoutingData" in self.line:
            ev = CallEvent(self.date,(self.getUcid()))
            ev.setDetails(self.getCallType())
    
    def agentStateChanged():
        return self.search(r"")

    def getUcid(self):
        return self.search(r"UCID<(.*?)>")

    def getCalling(self):
        return self.search(r"CallingDID:(.*?)\(S\)")

    def getDestination(self):
        return self.search(r"DestinationDID:(.*?)\(S\)")

    def getNewCallUcid(self):
        return (self.search(r"New Call object with UCID: (.*?)\s"))

    def getCallType(self):
        return self.search(r", CallTypeName:(.*?),")


    def getDiverted(self):
        return "Diverted Event," in self.line
        
    def getTransferred(self):
        return "Transferred Event," in self.line

    def getEstablished(self):
        return "Established Event," in self.line
        
    def getTerminated(self):
        return "Remove UCID<" in self.line
