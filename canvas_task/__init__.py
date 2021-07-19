from canvas_task.connect import createSess, write_info, fetch_course
import canvas_task.config as config

def main():
    sess=createSess(params={"access_token": config.token})
    write_info(fetch_course(sess))