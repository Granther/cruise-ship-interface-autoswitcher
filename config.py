import xml.etree.ElementTree as ET

class Config:
    def __init__(self):
        print('Instantiated Config')
        self.find_config()
        self.read_config()

    def read_config(self):
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
        except:
            print(f'ERROR: Unable to parse {self.configPath}')

    def find_config(self):
        self.configPath = 'config.xml'
