#!/usr/bin/python3
from subprocess import run
from datetime import datetime
from re import sub
from os import mkdir
from os.path import exists
from sys import exit

# commands for unzipping the templates
UNZIP_DAILY = ('unzip', 'daily.zip')
UNZIP_WEEKLY = ('unzip', 'weekly.zip')


# commands for removing templates
RM_DAILY = ('rm', 'daily.html')
RM_WEEKLY = ('rm', 'weekly.html')


# patterns for date formatting
FULL = '%B %-d, %Y'
FILE = '%-m-%-d'


# return the string representation of the date passed
def datestr(year:int, weeknum:int, daynum:int, pattern:str) -> str:
    return datetime.fromisocalendar(year, weeknum, daynum).strftime(pattern)


# return the week that the user wants to use for the templates
def week_info() -> tuple:
    # get the current year and week number
    year, weeknum = datetime.now().isocalendar()[:2]

    # generate info for current and following week
    curr_week = tuple((datestr(year, weeknum, i, FULL), (datestr(year, weeknum, i, FILE))) for i in range(1, 6))
    next_week = tuple((datestr(year, weeknum + 1, i, FULL), (datestr(year, weeknum + 1, i, FILE))) for i in range(1, 6))

    # store as two options in a dictionary
    options = {1: curr_week, 2: next_week}

    # prompt user for what week they want to use
    print('Select week to generate templates for:')
    print(f'1: {curr_week[0][0]} - {curr_week[4][0]}')
    print(f'2: {next_week[0][0]} - {next_week[4][0]}')
    
    # attempt to return the requested week
    try:
        week = int(input('> '))
        print(f'{options[week] = }')

    # quit if invalid option is given
    except:
        print(f'\033[31mERROR\033[0m: Input must be \'1\' or \'2\'')
        exit()


# prompt user for new directory name
dir_name = str(input('Enter new directory name: '))


# check if directory already exists
if exists(dir_name):
    print(f'\033[31mERROR:\033[0m directory \'{dir_name}\' already exists')
    exit()


# get the team name
team_name = str(input('Enter team name: '))


# get the week to be used for the templates
week = week_info()


# create the new directory
mkdir(dir_name)


# unzip the html zips
run(UNZIP_DAILY)
run(UNZIP_WEEKLY)


# open the 'daily.html' file and read its contents
with open('daily.html', 'r') as dhtml:
    
    # read in all contents of the file
    daily_html = dhtml.read()
    
    # loop through each day of the week
    for date, file_name in week:
        
        # substitute in the date and team name
        updated_html = sub(r'{DATE}', date, daily_html)
        updated_html = sub(r'{TEAM NAME}', team_name, updated_html)

        # save the updated html into the new file
        with open(f'{dir_name}/{file_name}.html', 'w') as newfile:
            newfile.write(updated_html)

# open weekly.html file and read in its contents
with open('weekly.html', 'r') as whtml:

    # read in all contents of the file
    weekly_html = whtml.read()

    # substitute in Monday and Friday's date
    updated_html = sub(r'{MON}', week[0][0], weekly_html)
    updated_html = sub(r'{FRI}', week[4][0], updated_html)

    # save the updated html into a new file
    with open(f'{dir_name}/{week[0][1]}_{week[4][1]}.html', 'w') as newfile:
        newfile.write(updated_html)


# remove the template files
run(RM_DAILY)
run(RM_WEEKLY)
