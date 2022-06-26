import canvas_task
from datetime import datetime
from json import load
from typing import List

from typer import Typer, echo
from canvas_task import connect
from .display import display
app = Typer(add_completion=False)
from .connect import createSess, write_info, fetch_course
import canvas_task.config as config
import os
import time
@app.command('refresh')
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

@app.command('update')
def update():
    refresh_data()
    read_data()

@app.command('read')
def read_data():
    with open(config.data_folder+'data.json','r') as file:
        display(load(file))

@app.command('ignore')
def ignore_assi(assi_id:int):
    connect.add_handsub
