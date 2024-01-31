"""Debug functions"""
import os
from datetime import datetime

DEBUG_DIR = os.path.abspath(os.path.dirname(__file__))

def dump_to_file(content: str,
                 filename: str='dump.html',
                 terminate: bool=True) -> None:
    
    with open(f'{DEBUG_DIR}/{filename}', 'w') as file:
        file.write(str(content))

    if terminate:
        print('Debug: terminate')
        exit(0)

def add_to_file(content: str, filename: str='flow.html') -> None:
    with open(f'{DEBUG_DIR}/{filename}', 'a') as file:
        file.write(f'{str(content)}\n\n')

def log(messgae: str) -> None:

    event = f'{datetime.now().strftime("%d.%m %H:%M:%S")} {messgae}'
    
    with open(f'logs/{datetime.now().strftime("%m-%d-%Y")}.txt', 'a') as file:
        file.write(f'{event}\n')
        
    print(event)