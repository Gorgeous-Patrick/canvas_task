from datetime import datetime
from json import load

import connect
from display import display
from connect import createSess, write_info, fetch_course
import config
import os
import time
import sys

def refresh_data():
    if not os.path.isfile(config.data_folder+'paper_submitted.json'):
        if not os.path.isdir(config.data_folder):
            os.mkdir(config.data_folder)
        open(config.data_folder+'paper_submitted.json','w').write('[]')
    sess=createSess(params={"access_token": config.token})
    try:
        write_info(fetch_course(sess))
    except Exception as e:
        print(e)
        time.sleep(10)
        refresh_data()


def update():
    refresh_data()
    read_data()


def read_data():
    with open(config.data_folder+'data.json','r') as file:
        display(load(file))


def ignore_assi(assi_id:int):
    connect.add_handsub

if __name__ == '__main__':

    if sys.argv[1]=='read':
        read_data()
    elif sys.argv[1]=='update':
        refresh_data()
    else:
        print('Invalid Command.')
