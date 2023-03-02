from threading import Thread
from multiprocessing import Process
from datetime import datetime
from rich.console import Console
from rich.panel import Panel

rc = Console()


def lucky_tickets_count(from_num: int, to_num: int, worker='Main process'):
    start = datetime.now()
    count = 0
    for i in range(from_num, to_num+1):
        ticket_number = str(i)
        while len(ticket_number) < 6:
            ticket_number = '0' + ticket_number
        if sum(map(int, ticket_number[:3])) == sum(map(int, ticket_number[3:])):
            count += 1
    rc.print('Count: ', count, style='bold white on green')
    end = datetime.now()
    rc.print(f'Execution time {worker}:', end-start, style='bold red')


rc.print(Panel('For getting a number of "lucky tickets" you have to enter four numbers of tickets '
               'number\'s range (no more 6 digits per number).\n'
               'Or type "exit" to exit the application',
               style='bold rgb(36,3,89) on rgb(252,246,123)',
               title="""Count of lucky ticket's number"""
               ))
while True:
    first_param = rc.input('\nPlease input the number of the first range from: ')
    if first_param == 'exit':
        break

    second_param = rc.input('Please input the number of the second range from: ')
    if second_param == 'exit':
        break

    if len(first_param) > 6 or len(second_param) > 6:
        rc.print('You have entered the wrong ticket number. Please, try again and be careful',
                 style='blink bold red')
        continue

    third_param = rc.input('Please input the number of the third range from: ')
    if first_param == 'exit':
        break

    fourth_param = rc.input('Please input the number of the fourth range from: ')
    if second_param == 'exit':
        break

    if len(third_param) > 6 or len(fourth_param) > 6:
        rc.print('You have entered the wrong ticket number. Please, try again and be careful',
                 style='blink bold red')
        continue

    try:
        from_number1 = int(first_param)
        to_number1 = int(second_param)
        from_number2 = int(third_param)
        to_number2 = int(fourth_param)
    except Exception as err:
        raise err

    lucky_tickets_count(from_number1, to_number1, worker='Main process 1')
    lucky_tickets_count(from_number2, to_number2, worker='Main process 2')

    thread1 = Thread(target=lucky_tickets_count, kwargs={'from_num': from_number1,
                                                         'to_num': to_number1,
                                                         'worker': 'thread1'})
    thread2 = Thread(target=lucky_tickets_count, kwargs={'from_num': from_number2,
                                                         'to_num': to_number2,
                                                         'worker': 'thread2'})

    process1 = Process(target=lucky_tickets_count, kwargs={'from_num': from_number1,
                                                           'to_num': to_number1,
                                                           'worker': 'process1'})
    process2 = Process(target=lucky_tickets_count, kwargs={'from_num': from_number2,
                                                           'to_num': to_number2,
                                                           'worker': 'process2'})

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    continue
