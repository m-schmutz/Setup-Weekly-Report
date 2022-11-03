#!/usr/bin/python3
from subprocess import run
from datetime import datetime
from re import subn
from os import mkdir

UNZIP_DAILY = ('unzip', 'daily.zip')
UNZIP_WEEKLY = ('unzip', 'weekly.zip')


    
# # prompt user for new directory name
# dir_name = str(input('Enter name for new directory: '))

# # get the team name
# team_name = str(input('Enter team name: '))

# # create the new directory
# mkdir(dir_name)

# unzip the html zips
run(UNZIP_DAILY)
run(UNZIP_WEEKLY)

# get the current week number and year
year, week_number = datetime.now().isocalendar()[:2]



