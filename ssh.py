from ping import *
from config import Config
from log import Log

class AntennaSSH:
    def __init__(self, host: str, user: str, pwd: str):
        log = Log('AntennaSSH')
        config = Config()

        if not attempt_multiple(config.ping_attempts):
            log.write_log(f"Couldn't ping {host} after {config.ping_attempts} tries")

        

