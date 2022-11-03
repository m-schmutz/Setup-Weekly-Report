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


# # prompt user for new directory name
dir_name = str(input('Enter new directory name: '))


# check if directory already exists
if exists(dir_name):
    print(f'\033[31mERROR:\033[0m directory \'{dir_name}\' already exists')
    exit()


# get the team name
team_name = str(input('Enter team name: '))


# check if user wants to generate templates for next week
next = str(input('Generate templates for next week? (y/n)')) == 'y'


# create the new directory
mkdir(dir_name)


# unzip the html zips
run(UNZIP_DAILY)
run(UNZIP_WEEKLY)


# get the current week number and year
year, week_number = datetime.now().isocalendar()[:2]


# create a tuple of the days of the week
days_of_week = tuple(datetime.fromisocalendar(year, week_number+next, i).strftime('%B %-d, %Y') for i in range(1, 6))


# create a tuple of the file names for each html file
date_file_names = tuple(datetime.fromisocalendar(year, week_number+next, i).strftime('%-m-%-d') for i in range(1, 6))


# open the 'daily.html' file and read its contents
with open('daily.html', 'r') as dhtml:
    
    # read in all contents of the file
    daily_html = dhtml.read()
    
    # 
    for date, file_name in zip(days_of_week, date_file_names):
        
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
    updated_html = sub(r'{MON}', days_of_week[0], weekly_html)
    updated_html = sub(r'{FRI}', days_of_week[4], updated_html)

    # save the updated html into a new file
    with open(f'{dir_name}/{date_file_names[0]}_{date_file_names[4]}.html', 'w') as newfile:
        newfile.write(updated_html)


# remove the template files
run(RM_DAILY)
run(RM_WEEKLY)
