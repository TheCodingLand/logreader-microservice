import json
import requests

class CallEvent(object):

    
    def __init__(self, date, id):
        self.id = id
        self.timestamp = date
        self.headers = {'content-type': 'application/json'}
        
    def add(date, id):
        headers = {'content-type': 'application/json'}
        url = "/evtmgr/call/"
        data = { 'timestamp' : "%s" % date, 'id' : id }
        print ("%s"% date)
        #requests.post(url, json.dumps(data),self.headers)
        print ("url :%s, data : %s headers : %s" % (url, json.dumps(data),headers))

        
    
    def setDetails(self, calltype):
        
        print ("sending request, timestamp : %s to change calltype for call %s to %s" % (self.timestamp, self.id, calltype))
        
