"""Debug functions"""
import os

DEBUG_DIR = os.path.abspath(os.path.dirname(__file__))

def dump_to_file(content,
                 filename='dump.html',
                 terminate=True):
        
    with open(f'{DEBUG_DIR}/{filename}', 'w') as file:
        file.write(str(content))

    if terminate:
        print('Debug: terminate')
        exit(0)

def add_to_file(content, filename='flow.html'):
    with open(f'{DEBUG_DIR}/{filename}', 'a') as file:
        file.write(f'{str(content)}\n\n')