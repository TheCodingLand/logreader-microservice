#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import requests
import threading
from project.log_parser.telephony_log import TelephonyLog
   

if os.getenv('LOGFILE'):
    logfile = os.environ['LOGFILE']
else:
    logfile = '/media/callcenter/DIAGS/TelephonyServer_ccrcsl02.000'


class parseLog(threading.Thread):

    def __init__(self, logfile):
        threading.Thread.__init__(self)
        self.kill_received = False
        self.LogFile = logfile
        self.line = ""
        self.num_lines = 0
        self.filesize = 0
        self.oldfilesize = 0
        self.f = ""
        self.percent = 0
    def parseline(self):
        e=TelephonyLog(self.line)    
        e.parse()
    def run(self):

        self.f = open(self.LogFile)
        
        self.num_lines = sum(1 for line in self.f)
        self.f.close()
        self.f = open(self.LogFile)
        self.filesize = os.stat(self.LogFile).st_size
        self.oldfilesize = self.filesize

        while not self.kill_received:
            self.filesize = os.stat(self.LogFile).st_size
            if self.filesize < self.oldfilesize:  # check if file has been rotated
                self.f.close()
                self.f = open(self.LogFile)
            self.oldfilesize = self.filesize
            self.line = self.f.readline()
            if self.line != '':
                self.parseline()
                time.sleep(.001)
                self.percent = (self.f.tell()/self.filesize)*100
                #print('%s : log at line %s %%' % (self.LogFile.split("/")[-1], self.percent))

        self.f.close()

thread = parseLog(logfile)
thread.start()

