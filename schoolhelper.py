import os

selection = 0


def school_schedule():
    print('Welcome to the school schedule! ')
    print('Here are the options: ')
    print('1. Show selected schedule. ')
    print('2. Create a new schedule. ')
    selection = int(input('Enter one of the options. '))

    if selection == 1:
        pass

    if selection == 2:
        schedule_name = input('Enter the name of the new schedule: ').lower()
        school_hours = int(input('Enter how many school hours you have. '))
        monday_file = f'schedules/{schedule_name}' + 'monday' + '.txt'
        tuesday_file = f'schedules/{schedule_name}' + 'tuesday' + '.txt'
        wednesday_file = f'schedules/{schedule_name}' + 'wednesday' + '.txt'
        thursday_file = f'schedules/{schedule_name}' + 'thursday' + '.txt'
        friday_file = f'schedules/{schedule_name}' + 'friday' + '.txt'


def homepage(selection):
    print('Welcome to the School Helper!')
    print('Here are the options: ')
    print('1. School Schedule')
    print('2. Homework')
    selection = int(input('Enter one of the options. '))
    if selection == 1:
        school_schedule()
    if selection == 2:
        pass


homepage(selection)
