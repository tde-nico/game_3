import threading
from time import sleep


def read_file(file_name):
    file = open(file_name, 'r')
    file_datas = file.read()
    file.close()
    return file_datas


def write_file(file_name, file_datas):
    file = open(file_name, 'w')
    file.write(file_datas)
    file.close()
	


def invoked_function(entity, variable, new_value):
    setattr(entity, variable, new_value)


def invoke(entity, variable, new_value, time_delay):
    thread = threading.Timer(time_delay, invoked_function, args=(entity, variable, new_value))
    thread.start()

