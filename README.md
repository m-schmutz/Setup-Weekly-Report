# Setup-Weekly-Report

#### This script is used to generate the template HTML files that are used for Weekly and Daily reports. It will also create a new directory to store the templates in.

## Use

#### If the script is executible, script can be ran with: `$ ./gen_templates.py`.
#### Otherwise it can be ran with python3: `$ python3 gen_templates.py`.

## Input
### Once ran the script will input for 3 things: 

### Directory Name

#### Prompt: 
```
Enter directory name to store templates:
```

#### The input given will be used to create a new directory in the current directory that will store all of the templates.
#### If the name given already exists in the current directory, an error is raised and the script will exit.

### Team Name
#### Prompt: 
```
Enter team name:
```

#### The input given will be used as the team name in the generated templates

### Week 
#### To get the week used in the templates, the script will ask whether the current or next week should be used:

#### Prompt: 
```
Select week to generate templates for: 
1: <Month> <Day>, <Year> - <Month> <Day>, <Year> # current week
2: <Month> <Day>, <Year> - <Month> <Day>, <Year> # following week
```

#### The corresponding month name, day, and year will be printed for each date. 
#### Entering 1 will generate templates for the current week
#### Entering 2 will generate templates for the following week


### Example picking week:

#### If the current date is November 6, 2022, the options printed out for week will be:
```
Select week to generate templates for:
1: November 7, 2022 - November 11, 2022
2: November 14, 2022 - November 18, 2022
```

#### *If user enters 1, the templates will be generated for November 7, 2022 through November 11, 2022*

#### *If user enters 2, the templates will be generated for November 14, 2022 through November 18, 2022*

