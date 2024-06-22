import paramiko

from ping import *
from config import Config
from log import Log
#from utils import AntennaSSHException

class AntennaSSHException(Exception):
    def __init__(self, message):
        super().__init__(message)

class AntennaSSH:
    def __init__(self, host: str, user: str, pwd: str, log: Log = None, config: Config = None):
        self.log = log or Log('AntennaSSH')
        self.config = config or Config()

        self.user = user
        self.pwd = pwd
        self.host = host

        if not attempt_multiple(int(self.config.ping_attempts), self.host):
            self.log.write_log(f"Couldn't ping {self.host} after {self.config.ping_attempts} tries")
            raise AntennaSSHException('Unable to connect to host')
    
    def connect_ssh(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.connect(self.host,
                        username=self.user,
                        password=self.pwd,
                        look_for_keys=True)
        except Exception as e:
            self.log.write_log(f"Error connecting/creating ssh with host: {self.host}. ERRCOD:{str(e)}")
            raise AntennaSSHException(f'Exception occured when connecting the host {self.host}. Futher info: {str(e)}')
        
        return ssh
        
    def send_command(self, command: str):
        try:
            ssh = self.connect_ssh()
        except AntennaSSHException as e:
            raise

        try:
            return ssh.exec_command(command)
        except Exception as e:
            raise AntennaSSHException(f'Exception occured when executing remote host command. Further info: {str(e)}')




an = AntennaSSH('192.168.1.172', 'grant', 'bowieboom123')

un, dos, tre = an.send_command('ip a')


