import ping3

def ping(host, timeout=1.5):
    reponseTime = ping3.ping(host, timeout=timeout)

    if reponseTime == None:
        return False
    
    return reponseTime * 1000

def attempt_multiple(n_times: int, host: str):
    for _ in range(n_times):
        response = ping(host)
        if response:
            return response
        
    return False

