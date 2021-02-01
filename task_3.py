import os
import uuid

def ping():
    with open('devices.txt') as file:
        dump = file.read()
        lines = dump.splitlines()

    for line in lines:
        ip = (str(line).split('-', 1)[1]).replace(" ", "")
        ping_result_file = f'ping_result#{uuid.uuid4()}.txt'
        return os.system(f'ping {ip} >> {ping_result_file}')

ping()
