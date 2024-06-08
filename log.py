import sys
import os

class Log:
    def __init__(self):
        try:
            self.find_logfile()
        except:
            print('ERROR: Error encountered while instantiating logs')
            sys.exit(1)

    def find_logfile(self):
        self.logfile = 'logs.txt'

        if self.logfile == None:
            raise Exception
        
        return True
    
    def write_log(self, log):
        try:
            file = open(self.logfile, 'w')
            file.write(log)
            file.close()
        except:
            return False
        
        return True
