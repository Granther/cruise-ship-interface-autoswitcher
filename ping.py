import ping3
from log import LogException

class PingException(LogException):
    def __init__(self, message):
        super().__init__(message)

def ping(host, timeout=1.5):
    try:
        reponseTime = ping3.ping(host, timeout=timeout)
    except OSError:
        return 999
    except Exception as e:
        raise PingException(f'Exception occured when attempting to ping host {host}') from e

    return int(reponseTime * 1000)
    
def attempt_multiple(n_times: int, host: str):
    for _ in range(n_times):
        response = ping(host)
        if response:
            return response
        
    return False

