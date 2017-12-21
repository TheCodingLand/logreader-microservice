from re import search
from datetime import datetime
from time import strptime,mktime

class LogLine(object):

    line= str()
    events = []
    
    def __init__(self, line):
        self.line = line
     
    def search(self,rx):
        try:
            r = search(rx, self.line)
            return r.group(1)
        except:
            
            return False

    def getDate(self):
        s = self.search("^\[(.*?)\.")
        d=False
        if s:
            t = strptime(s, '%Y/%m/%d %H:%M:%S')
            d = datetime.fromtimestamp(mktime(t))
        return d
    