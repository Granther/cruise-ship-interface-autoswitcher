import xml.etree.ElementTree as ET
from log import Log, LogException

class ConfigFileException(LogException):
    def __init__(self, message):
        super().__init__(message)

class ConfigPermissionException(LogException):
    def __init__(self, message):
        super().__init__(message)

class ConfigException(LogException):
    def __init__(self, message):
        super().__init__(message)

class Config:
    def __init__(self):
        self.log = Log('Config')

        try:
            self.find_config()
        except (ConfigFileException, ConfigPermissionException):
            try:
                self.generate_config()
            except (ConfigFileException, ConfigPermissionException) as e:
                raise ConfigException(f'Unable to read/access config file {self.configPath}') from e
            
        self.read_config()

    def read_config(self):
        if self.configPath == None:
            self.log.write_log('here')
            self.log.write_log(f'ERROR: Unable to parse {self.configPath}, using hard coded Config. I DO NOT RECOMMEND THIS!!')

        try:
            tree = ET.parse(self.configPath)
            root = tree.getroot()

            self.lr_ssh_user = root[0].text
            self.lr_ssh_pwd = root[1].text
            self.lr_ip = root[2].text

            self.sr_ssh_user = root[3].text
            self.sr_ssh_pwd = root[4].text
            self.sr_ip = root[5].text

            self.beep_timeout = root[6].text
            self.ping_attempts = root[7].text
            self.beep_delay = root[8].text
            self.leaving_wait_aving_wait_time = root[9].text
            self.host_to_ping = root[10].text
            self.ping_interval = int(root[11].text)
            self.periodic_check_interval = int(root[12].text)

            self.yellow_ping_threshold = int(root[13].text)
            self.green_ping_threshold = int(root[14].text)

        except:
            self.log.write_log(f'ERROR: Unable to parse {self.configPath}, using hard coded Config. I DO NOT RECOMMEND THIS!!')            


    def find_config(self):
        try:
            self.configPath = 'config.xml'
            file = open(self.configPath, 'r')
        except FileNotFoundError as e:
            raise ConfigFileException(f'Exception raised when locating {self.configPath} for instantiation') from e
        except PermissionError as e:
            raise ConfigPermissionException(f'User lacks permissions to read {self.configPath}') from e
        except Exception as e:
            raise ConfigFileException(f'Exception occured when finding config {self.configPath}') from e

    def generate_config(self):
        try:
            self.configPath = 'config.xml'
            file = open(self.configPath, 'wr')
            file.write(self.config_template)
            file.close()
            self.log.write_log(f'Generated config file from {self.configPath}')
        except PermissionError as e:
            raise ConfigPermissionException(f'User lacks permissions to read/write {self.configPath}') from e
        except Exception as e:
            raise ConfigFileException(f'Exception occured when creating config {self.configPath}') from e

