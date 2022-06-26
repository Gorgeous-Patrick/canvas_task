import time

def display(data):
    refreshed_time=data['refreshed_at']
    flattened=create_assignment_list(data['info'])
    flattened.sort(key=cmptime)
    print('Notification (Refreshed at %s):\n'%(time.asctime(time.localtime(refreshed_time))))
    for assi in flattened:
        print_assi(assi)

def cmptime(elem):
    return time.mktime(time.strptime(elem['due'], '%Y-%m-%dT%H:%M:%SZ'))

def create_assignment_list(data):
    res=[]
    for course in data:
        for assi in course['assignments']:
            assi['course_code']=course['code']
            assi['time_left']=time.mktime(time.strptime(assi['due'], '%Y-%m-%dT%H:%M:%SZ'))- time.time()+8*60*60
            res.append(assi)
    return res

def get_time_left(assi):
    t=round(assi['time_left'])
    sec=t%60
    min=(t//60)%60
    hour=(t//(60*60))%24
    day=round(t//(60*60*24))
    return ('Time Left:\t%d Days, %d Hours, %d Minute, %d Seconds' % (day, hour, min, sec))

def get_title(assi):
    return assi['course_code']+':\t\t'+assi['name']

def get_due_time(assi):
    t=time.mktime(time.strptime(assi['due'], '%Y-%m-%dT%H:%M:%SZ'))+ 8* 60 *60
    return time.asctime(time.localtime(t))

def print_assi(assi):
    print(get_title(assi))
    print('Due:\t\t', get_due_time(assi))
    print('ID:\t\t', assi['assignment_id'])
    print(get_time_left(assi))
    print('URL:\t\t', assi['url'])
    print("")
