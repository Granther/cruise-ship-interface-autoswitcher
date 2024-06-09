from log import Log, LogException
from config import Config
from ssh import AntennaSSH
    
class UtilParamException(LogException):
    def __init__(self, message):
        super().__init__(message)

class UtilRemoteCommandException(LogException):
    def __init__(self, message):
        super().__init__(message)

class AntennaSSHException(LogException):
    def __init__(self, message):
        super().__init__(message)

class Utils():

    antenna_states = {
        '0': 0,
        '1': 0
    }

    command_dict = {
        'reboot': 'reboot now',
        'link up': 'ip link set ath0 up',
        'link down': 'ip link set ath0 down',
        'link status': 'ip link show enp4s0',
        'ip a': 'ip a'
    }

    def __init__(self, config: Config = None):
        self.log = Log('Utils')
        self.config = config or Config

    def util_command(self, id, command):
        if id is 0:
            self.config.sr_ip = '192.168.1.172'
            self.config.sr_ssh_pwd = 'bowieboom123'
            self.config.sr_ssh_user = 'grant'
            conn = (self.config.sr_ip, self.config.sr_ssh_user, self.config.sr_ssh_pwd)
        elif id is 1:
            conn = (self.config.lr_ip, self.config.lr_ssh_user, self.config.lr_ssh_pwd)
        else:
            raise UtilParamException('Antenna ID was not 0 or 1')
        
        try:
            ssh = AntennaSSH(*conn)
            return ssh.send_command(self.command_dict[command])
        except AntennaSSHException as e:
            raise

    def iterate_std(self, _, stdout, stderr, fetch_word=None):
        if stderr != None:
            stderr_out = ''
            for line in stderr_out:
                stderr_out += line
            raise UtilRemoteCommandException(f'Remote command returned stderr: {stderr_out}')
        
        if fetch_word == None:
            return True

        try:
            for line in stdout:
                if fetch_word in line:
                    return line
        except Exception as e:
            raise UtilRemoteCommandException(f'Exception raised when iterating stdout. Further info: {str(e)}')

    def reboot(self, id):
        command_std = self.util_command(id, 'reboot')

        iterated = self.iterate_std(*command_std)

        if iterated:
            self.log.write_log(f'Rebooting host with ID of {id} remotely')
            return
        
    def ath0_status(self, id):
        command_std = self.util_command(id, 'link status')

        iterated = self.iterate_std(*command_std)
        
        if 'UP' in iterated:
            return 1
        elif 'DOWN' in iterated:
            return 0
        else:
            raise UtilRemoteCommandException(f'Antenna interface state does not appear in std: {iterated}', )

    def safe_switch(off=None, on=None):


    def switch_antenna(self, wait_time=None):
        sr_state = self.ath0_status(0)
        lr_state = self.ath0_status(1)

        if (sr_state + lr_state) == 2:
            self.log.write_log('Both interfaces are enabled!! Disabling SR Interface')
            self.inter_off(0)

        elif (sr_state + lr_state) == 0:
            self.log.write_log('Neither interface is enabled!! Enabling LR Interface')
            self.inter_on(1)

        elif sr_state == 1:
            self.log.write_log('Disabling SR, enabling LR')
            self.inter_off(0)
            time.sleep(5)
            self.inter_on(1)

        elif lr_state == 1:
            self.log.write_log('Disabling LR, enabling SR')
            self.inter_off(1)
            time.sleep(5)
            self.inter_on(0)
        else:
            pass

    def inter_off(self, host):
        try:
            self.util_command(id, 'link down')
        except AntennaSSHException as e:
            

    def inter_on(self, host):
        self.util_command(id, 'link up')

    def leaving(self, host):
        pass

util = Utils()
util.reboot(0)