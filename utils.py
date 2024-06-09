from log import Log
from config import Config
from ssh import AntennaSSH
    
class UtilParamException(Exception):
    def __init__(self, message):
        super().__init__(message)

class AntennaSSHException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Utils:

    command_dict = {
        'reboot': 'reboot now',
        'link': 'ip a'
    }

    def __init__(self):
        self.log = Log('Utils')
        self.config = Config

    def reboot(self, id):
        if id is 0:
            conn_info = (self.config.sr_ip, self.config.sr_ssh_user, self.config.sr_ssh_pwd)
        elif id is 1:
            conn_info = (self.config.lr_ip, self.config.lr_ssh_user, self.config.lr_ssh_pwd)
        else:
            raise UtilParamException('Antenna ID was not 0 or 1')
        
        try:
            ssh = AntennaSSH(conn_info)
            ssh.send_command(self.command_dict['reboot'])
        except AntennaSSHException as e:
            raise

    def switch_antenna(self):
        pass

    def inter_off(self, host):
        pass

    def leaving(self, host):
        pass