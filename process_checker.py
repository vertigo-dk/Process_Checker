#!/usr/bin/env python
__author__ = 'frederikjuutilainen'

import threading, time, json, psutil, os, sys

refresh_rate = 5.0 # time between checks

class Process:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.running = False

    def open(self):
        os.system('open ' + self.location)
        print('open ' + self.location)

def check_processes(data_list):
    processes = []
    # create list of Process from data_list
    for entry in data_list:
        p = Process(entry["process_name"],entry["app_location"])
        processes.append(p)

    while True:
        # check if processes are running
        for proc in psutil.process_iter():
            for p in processes:
                if proc.name().lower() == p.name.lower():
                    p.running = True

        # open all processes that are running
        for p in processes:
            if(p.running == False):
                p.open()
            p.running = False

        time.sleep(refresh_rate)

def main():
    # open json file
    with open('process_list.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    t = threading.Timer(1.0, check_processes(data))
    t.start()

if __name__ == "__main__":
    main()
