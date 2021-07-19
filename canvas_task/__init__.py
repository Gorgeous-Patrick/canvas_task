from canvas_task.connect import createSess, write_info, fetch_course
import canvas_task.config as config
import os
def main():
    if not os.path.isfile(config.data_folder+'paper_submitted.json'):
        if not os.path.isdir(config.data_folder):
            os.mkdir(config.data_folder)
        open(config.data_folder+'paper_submitted.json','w').write('[]')
    sess=createSess(params={"access_token": config.token})
    write_info(fetch_course(sess))