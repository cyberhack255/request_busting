#!/usr/bin/python3

from multiprocessing import Pool
from functools import partial
import re
import socket
import time
import argparse
import requests
import random
import lists



def req(id, config):
    print(id)
    for i in config:
        s = requests.session()
        while time.time() <= config['t_end']:
            url = f"https://{config['host']}{random.choice(lists.paths)}"
            print(url)
            match config['method']:
                case "GET":
                    s.get(url, headers={"X-CSOC-Client-IP":f"{random.choice(lists.attacking_ips)}","User-Agent": f"{random.choice(lists.attacking_user_agents)}"})
                case "POST":
                    s.post(url, headers={"X-CSOC-Client-IP":f"{random.choice(lists.attacking_ips)}","User-Agent": f"{random.choice(lists.attacking_user_agents)}"})
            time.sleep(0.15)
                
            #i = i + 1



def manager(config):
    print('''
______            _                                   _   _____          __  __ _        _____            
| ___ \          | |                                 | | |_   _|        / _|/ _(_)      |  __ \           
| |_/ / __ _  ___| | ____ _ _ __ ___  _   _ _ __   __| |   | |_ __ __ _| |_| |_ _  ___  | |  \/ ___ _ __  
| ___ \/ _` |/ __| |/ / _` | '__/ _ \| | | | '_ \ / _` |   | | '__/ _` |  _|  _| |/ __| | | __ / _ \ '_ \ 
| |_/ / (_| | (__|   < (_| | | | (_) | |_| | | | | (_| |   | | | | (_| | | | | | | (__  | |_\ \  __/ | | |
\____/ \__,_|\___|_|\_\__, |_|  \___/ \__,_|_| |_|\__,_|   \_/_|  \__,_|_| |_| |_|\___|  \____/\___|_| |_|
                       __/ |                                                                              
                      |___/    
''')
    t_end = time.time() +(config['t_end']* 3600)
    config['t_end'] = t_end
    with Pool(2) as p:
        path = partial(req, config=config)
        p.map(path, range(2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Traffic Generator",
    epilog='''

______            _                                   _   _____          __  __ _        _____            
| ___ \          | |                                 | | |_   _|        / _|/ _(_)      |  __ \           
| |_/ / __ _  ___| | ____ _ _ __ ___  _   _ _ __   __| |   | |_ __ __ _| |_| |_ _  ___  | |  \/ ___ _ __  
| ___ \/ _` |/ __| |/ / _` | '__/ _ \| | | | '_ \ / _` |   | | '__/ _` |  _|  _| |/ __| | | __ / _ \ '_ \ 
| |_/ / (_| | (__|   < (_| | | | (_) | |_| | | | | (_| |   | | | | (_| | | | | | | (__  | |_\ \  __/ | | |
\____/ \__,_|\___|_|\_\__, |_|  \___/ \__,_|_| |_|\__,_|   \_/_|  \__,_|_| |_| |_|\___|  \____/\___|_| |_|
                       __/ |                                                                              
                      |___/
''')
    parser.add_argument('--host', help="Host", type=str)
    parser.add_argument('-t', help= 'time in hours to run the traffic for', type=int)
    parser.add_argument('-m', help="Method to use GET or POST")
    args = parser.parse_args()
    if args.host is None: 
        print('Please provide a host')
        exit()
    
    config = {'host':args.host, 't_end': args.t, 'method': str.upper(args.m)}
    print(config)
    manager(config)
        
