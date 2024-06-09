import paramiko

from ping import *
from config import Config
from log import Log
from utils import AntennaSSHException

class AntennaSSH:
    def __init__(self, host: str, user: str, pwd: str):
        self.log = Log('AntennaSSH')
        self.config = Config()

        self.user = user
        self.pwd = pwd
        self.host = host

        if not attempt_multiple(int(self.config.ping_attempts), self.host):
            self.log.write_log(f"Couldn't ping {self.host} after {self.config.ping_attempts} tries")
    
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
        
    # def send_command(self, command):
    #     try:
    #         ssh = self.connect_ssh()
    #     except:


an = AntennaSSH('192.168.1.172', 'grant', 'bowieboom123')

