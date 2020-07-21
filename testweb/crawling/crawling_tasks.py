from background_task import background
import time
@background() # per second
def task_hello(schedule=1, repeat=2):
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    print("task ... Hello World!", time_str)