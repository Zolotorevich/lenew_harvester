from datetime import datetime


# Add any events to log file
def log(messgae:str):

    event = f'{datetime.now().strftime("%H:%M:%S")} {messgae}'
    
    with open(f'log.txt', 'a') as file:
        file.write(f'{event}\n')
        
    print(event)