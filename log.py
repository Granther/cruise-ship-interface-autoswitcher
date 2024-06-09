import os



class Log:
    def __init__(self, className: str):
        try:
            self.find_logfile()
        except Exception as e:
            print(f'ERROR: Error encountered while instantiating logs: {e}')
            return None
        
        self.className = className

    def find_logfile(self):
        
        self.logfile = 'logs.txt'
        
        return True
    
    def write_log(self, log):
        try:
            file = open(self.logfile, 'a')
            file.write(f'{self.className}: {log}\n')
            file.close()
        except:
            return False
        
        return True
    

