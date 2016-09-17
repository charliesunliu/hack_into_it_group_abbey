# hack_into_it_group_abbey
The program uses the American Community Survey 2015 dataset and the Quarterly Workforce Indicators dataset to quickly estimate a college graduate’s base salary dependent on their age, gender, state, education level and so on

This program runs in Python 2. It is composed of a single .py file, salary_predictor.py.

#### 1 #### Beginning Execution:

To run the program, run the file salary_predictor.py with Python. This will bring up the program screen, where you can input information.
The screen should look like:
=========
Enter your 2 letter state abbreviation: (or X for no state)
>
========
The user is expected to enter two capital letters representative of their state, and press enter.
Age will also be asked for, and the program expects a numerical value.

#### 2 #### Optional Parameters:

After the user enters their required state and age information, the program will ask the user to choose optional parameters to refine their search.
It will print:
========
Choose a field below by entering the number to the left of the fields.
	1. Select your Field of Interest
	2. Select your Race
	3. Select your Gender
	4. Select your education
	Enter 5 to exit setting variables
>
=======
To choose a field, the user will enter a number corresponding to the desired parameter. For example, a user will enter "1" to fill out their field of interest (See "Entering Parameter Fields").
The user can also finish and begin a salary estimation at any time by entering "5" on this screen (see "Finishing Input").

#### 3 #### Entering Parameter Fields:

When the user chooses to fill an optional parameter, the program will ask for specifics on their parameter.

For example, entering "1" will prompt the user to enter their field of interest.
The program will print:
=======
Enter an industry:
	1. Management/Business/Financial
	2. Computer/Engineering/Science
	3. Education/Legal/Community Service/Arts and Media Occupations
	4. Healthcare Practices and Technical Occupations
	5. Service Occupations
	6. Sales and Office Occupations
	7. Natural Resources, Conservation, and Maintenance Occupations
	8. Production, Transportation, and Material Moving
	9. Skip
>
=======
A similar screen will appear upon selecting one of the other optional parameters.
The user is expected to enter the number corresponding to the industry they are looking into, or "9" to skip entering the field and return to the parameter choosing section without choosing a field of interest.
Once a valid number has been entered, the program will return to the parameter choosing section.

#### 4 #### Finishing Input
Once the user has finished setting variables, the program will calculate an estimated salary based on their inputs to parameter fields.
This output will be displayed to the user, and the program will terminate.
