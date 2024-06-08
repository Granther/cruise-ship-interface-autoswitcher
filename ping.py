import ping3

def ping(host):
    try:
        reponseTime = ping3.ping(host)
    except:
        reponseTime = 0

    return reponseTime * 1000

#print(ping('10.10.1.1'))