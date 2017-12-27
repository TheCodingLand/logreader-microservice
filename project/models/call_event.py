import json

conn = redis.StrictRedis(host="redis", port=6379, db=0)
class CallEvent(object):

    def __init__(self, date, id):
        self.id = id
        self.timestamp = date
        self.headers = {'content-type': 'application/json'}

    def add(date, id):
        """storing a add call into redis"""
        data = { 'action': 'add', 'timestamp' : "%s" % date, 'id' : id }
        conn.hmset("pythonDict", data)


    def setDetails(self, calltype):
        data = { 'action': 'setdetails', 'timestamp' : "%s" % self.timestamp, 'id' : self.id, 'data' : self.calltype }
        conn.hmset("pythonDict", data)