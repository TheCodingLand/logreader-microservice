from re import search
from datetime import datetime
from time import strptime,mktime
import base64


class LogLine(object):

    line= str()
    events = []
    
    def __init__(self, line):
        self.hash = base64.b64encode(hashlib.md5(line).digest())
        self.line = line
     
    def search(self,rx):
        try:
            r = search(rx, self.line)
            return r.group(1)
        except:
            
            return False

    def getDate(self):
        s = self.search("^\[(.*?)\]")
        d=False
        if s:
            t = strptime(s, '%Y/%m/%d %H:%M:%S.%f')
            d = datetime.fromtimestamp(mktime(t))
        return d
    
