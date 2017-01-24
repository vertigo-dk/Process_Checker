#!/usr/bin/env python
__author__ = 'frederikjuutilainen'

import threading, time, json, psutil, os

class Process:
    def __init__(self, name):
        self.name = name
        self.running = False

def check_processes(data_list):
    processes = []
    # create list of Process from data_list
    for p_name in data_list["processes"]:
        p = Process(p_name)
        processes.append(p)

    while True:
        # kill unresponsive
        os.system('sudo ./killunresponsive/killunresponsive')

        # check if processes are running
        for proc in psutil.process_iter():
            for p in processes:
                if proc.name() == p.name:
                    p.running = True

        # open all processes that are running
        for p in processes:
            if(p.running == False):
                print(p.name + " not running")


        time.sleep(5.0)

def main():
    with open('process_list.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    t = threading.Timer(1.0, check_processes(data))
    t.start()

if __name__ == "__main__":
    main()
