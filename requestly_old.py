#!/usr/bin/python3

from multiprocessing import Pool
from functools import partial
import socket
import time
import argparse


def req(id, config):
    print(id)
    for i in config:
        while time.time() <= config['t_end']:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((config['host'], config['port']))
            data = f"{config['method']} {config['path']} HTTP/1.1\r\nHost:{config['host']}\r\n\r\n".encode()
            sock.send(data)
            resp = sock.recv(1024)
            print(resp)
            #i = i + 1
            sock.close()


def manager(config):
    print('''
  _____                            _   _       
 |  __ \                          | | | |      
 | |__) |___  __ _ _   _  ___  ___| |_| |_   _ 
 |  _  // _ \/ _` | | | |/ _ \/ __| __| | | | |
 | | \ \  __/ (_| | |_| |  __/\__ \ |_| | |_| |
 |_|  \_\___|\__, |\__,_|\___||___/\__|_|\__, |
                | |                       __/ |
                |_|                      |___/        
''')
    print(f"Starting Requests to {config['host']}:{config['port']}{config['path']} for {config['t_end']} seconds")
    t_end = time.time() + config['t_end']
    config['t_end'] = t_end
    with Pool(30) as p:
        path = partial(req, config=config)
        p.map(path,range(30))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Traffic Generator",
    epilog='''

  _____                            _   _       
 |  __ \                          | | | |      
 | |__) |___  __ _ _   _  ___  ___| |_| |_   _ 
 |  _  // _ \/ _` | | | |/ _ \/ __| __| | | | |
 | | \ \  __/ (_| | |_| |  __/\__ \ |_| | |_| |
 |_|  \_\___|\__, |\__,_|\___||___/\__|_|\__, |
                | |                       __/ |
                |_|                      |___/ 
               
''')
    parser.add_argument('--host', help="Host", type=str)
    parser.add_argument('--path', help='Path', type=str)
    parser.add_argument('-p', help= 'port', type=int)
    parser.add_argument('-m', help= 'method', type=str)
    parser.add_argument('-t', help= 'time in seconds to run the traffic for', type=int)
    args = parser.parse_args()
    if args.host is None: 
        print('Please provide a host')
        exit()
    
    config = {'host':args.host, 'path': args.path, 'method': str.upper(args.m), 't_end': args.t, 'port': args.p}
    print(config)
    manager(config)
        
