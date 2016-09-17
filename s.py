#import numpy
from numpy import array,ones,linalg
from pylab import plot,show
import numpy
import requests
import urllib2

#census_variables = ['NAME'] #we're going to append to this with return values from choose_* functions


#choose_area(),choose_gender(),choose_race(),choose_industry(),choose_age(),choose_ed()

area_p = None
age_p = None
industry_p = None
gender_p = None
ed_p = None
race_p = None



#-------------------Indivicual Variables-----------------------#
#returns None if user chooses not to choose an industry
#otherwise returns the full industry_param
def choose_industry():
  industry_param = 'B24011_0'
  industry_mapping = {1: '03E', 2: '06E', 3: '10E', 4: '15E', 5: '18E', 6: '26E', 7: '29E', 8: '33E', 9: None}
  print "Enter an industry: "
  print "1. Management/Business/Financial\n", \
        "2. Computer/Engineering/Science\n", \
        "3. Education/Legal/Communicaty Service/Arts and Media Occupations\n", \
        "4. Healthcare Practices and Technical Occupations\n", \
            "5. Service Occupations\n", \
            "6. Sales and Office Occupations\n", \
            "7. Natural Resources, Conservation, and Maintenance Occupations\n", \
        "8. Production, Transportation, and Material Moving Occupations\n", \
        "9. Skip\n\n"
  industry_choice = int(raw_input())
  while industry_choice not in industry_mapping.keys():
    print "Sorry, ", industry_choice, "is not in our database. Try again."
    industry_choice = int(raw_input())
  if industry_choice == 9:
      return None

  industry_param += industry_mapping[industry_choice]
  return industry_param

#returns None if user chooses not to choose a race
#otherwise returns the full race_param
def choose_race():
  race_param = "B20017"
  race_mapping = {1:  'A_001E', 2: 'B_001E', 3: 'C_001E', 4: 'D_001E', 5: 'E_001E', 6: 'I_001E', 7: 'F_001E', 8: None}
  print "Enter your race: "
  print "1. White\n", \
        "2. Black or African American\n", \
        "3. American Indian and Alaskan Native\n", \
        "4. Asian\n", \
        "5. Native Hawaiian and Other Pacific Islander\n", \
        "6. Hispanic or Latino or Latino\n", \
        "7. Other\n", \
        "8. Skip\n\n"
  race_choice = int(raw_input())

  while race_choice not in race_mapping.keys():
    print "Sorry, ", race_choice, "is not in our database. Try again."
    race_choice = int(raw_input())
  if race_choice == 8:
    return None

  race_param += race_mapping[race_choice]
  return race_param


#returns None if user chooses not to choose a gender
#otherwise returns the full gender_param
def choose_gender():
  gender_param = "B24012_0"
  gender_mapping = {1: '02E', 2: '38E', 3: None, 4: None}
  print "Enter your gender: "
  print "1. Male\n", \
        "2. Female\n", \
            "3. Other\n", \
        "4. Skip\n\n"
  gender_choice = int(raw_input())
  while gender_choice not in gender_mapping.keys():
    print "Sorry, ", gender_choice, "is not in our database. Try again."
    gender_choice = int(raw_input())
  if gender_choice == 3 or gender_choice == 4:
    return None

  gender_param += gender_mapping[gender_choice]
  return gender_param

def choose_ed():
  ed_param = "B20004_00"
  ed_mapping = {1: '5E', 2: '6E', 3: None}
  print "Enter your education level: "
  print "1. Bachelor's Degree\n", \
            "2. Graduate or Professional Degree\n", \
            "3. Skip\n\n"
  ed_choice = int(raw_input())
  while ed_choice not in ed_mapping.keys():
    print "Sorry, ", ed_choice, "is not in our database. Try again."
    ed_choice = int(raw_input())
  if ed_choice == 3:
    return None

  ed_param += ed_mapping[ed_choice]
  return ed_param

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
statenumbers = ['01','02','04','05','06','08','09','10','11','12','13','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','44','45','46','47','48','49','50','51','53','54','55','56']

def requiredinfo():
  print "Enter your 2 letter state abbreviation: (or X for no state)"
  area = str(raw_input())
  while area not in states and area != 'X':
    print "Sorry, ", area, "is not a valid state. Try again."
    area = str(raw_input())
  print "Enter your age: "
  age = int(raw_input())
  while not age:
    print "Sorry, ", age, "is not a valid age. Try again."
    age = int(raw_input())
  if age <= 24:
    agecode = 'A03' #sets user's salary based on that of 22-24 age group
  else:
    agecode = 'A04' #sets user's salary based on that of 25-34 age group
  basesalary = 0
  yearsalary = [0,0,0,0,0]
  quartersalary = 0
  increase_rate = [0.0,0.0,0.0,0.0]
  if area != 'X':
    for x in range(2010,2015):
      for y in range(1,5):
        year = str(x)
        quarter = str(y)
        url = 'http://api.census.gov/data/timeseries/qwi/sa?get=EarnS&for=state:' + statenumbers[states.index(area)] + '&year=' + year + '&quarter=' + quarter + '&agegrp=' + agecode + '&key=12d01c707d06d007959c6906293ee268eff111d2'
        response = urllib2.urlopen(url)
        data = response.read()
        text = data.decode()
        quartersalary = int(text[48:52])
        yearsalary[x-2010] += quartersalary*3
        print(x,y)
        print(quartersalary)
      basesalary = basesalary + yearsalary[x-2010]
  basesalary = basesalary/5
  if area!= 'X':
  	for x in range(0,4):
  	  increase_rate[x] = (float(yearsalary[x+1]) - float(yearsalary[x]))/float(yearsalary[x+1])
  	  increase_rate = sum(increase_rate)
  print(increase_rate)
  print(yearsalary)
  print(basesalary)



  return age,agecode,area, basesalary,increase_rate

age,agecode,area, basesalary,increase_rate = requiredinfo()

#-------------------Variable Choice-----------------------#
def blah(basesalary):
  choice = None #User choice for adding what variables.
  #choose_area(),choose_gender(),choose_race(),choose_industry(),choose_age(),choose_ed()
  to_append = []
  print "now in main before while loop\n"
  while choice != 9:
    print "Choose a field below by entering the number to the left of the fields. \n"
    print "1. Select your Field of Interest\n", \
    "2. Select your Race\n", \
    "3. Select your Gender\n", \
    "4. Select your education\n", \
    "Enter 5 to exit setting variables,"
    choice = int(raw_input())
    #print "u chose", choice
    if choice == 1:
      global industry_p
      industry_p = choose_industry()
    elif choice == 2:
      global race_p
      print "in choice 4!"
      print "race_p is currently:", race_p
      race_p = choose_race()
      print "race_p is now: ", race_p
    elif choice == 3:
      global gender_p
      gender_p = choose_gender()
    elif choice == 4:
      global ed_p
      ed_p = choose_ed()
    elif choice == 5:
        #if (not area_p) or (not age_chosen):
        #  print "You haven't chosen your age/area yet!"
        #  choice = 0
        #else:
        #  break
        break
    else:
        print("The choice is invalid, please try again.")



#-------------------Main-----------------------#


  census_variables = ['NAME']
  counter = 0
  #for each of the _params that aren't None, append them to census_variable
  if industry_p:
    census_variables.append(industry_p)
    counter += 1
  if race_p:
    census_variables.append(race_p)
    counter += 1
  if gender_p:
    census_variables.append(gender_p)
    counter += 1
  if ed_p:
    census_variables.append(ed_p)
    census_variables.append('B20004_001E')
    counter += 1

  census_variables.append('B24012_001E')
  #print "census_variables: ", census_variables

#24123

  params = {
      'get': ','.join(census_variables),
      'for': 'state:*',
      'key': 'a0b4975367ed6e3cd0655707d1385def9b546d85'
  }

  data = requests.get("http://api.census.gov/data/2015/acs1", params=params)
  interesting = 0
  statesalary = 0
  projectedsalarylist = []
  originalcounter = counter
  elemcounter = 0
  a = 0
  if area == 'X':
      for elem in data.json():
          counter = originalcounter
          if str(elem[0]) != 'NAME':
              url = 'http://api.census.gov/data/timeseries/qwi/sa?get=EarnS&for=state:' + statenumbers[elemcounter] + '&year=2012&quarter=1&agegrp=' + agecode + '&key=12d01c707d06d007959c6906293ee268eff111d2'
              response = urllib2.urlopen(url)
              data = response.read()
              text = data.decode()
              basesalary = int(text[48:52]) * 12
              ratio = 1.0000
              if 'B20004_001E' in census_variables:
                  ratio = ratio * (float(elem[census_variables.index('B20004_001E')-1]) / float(elem[census_variables.index('B20004_001E')]))
              while counter:
                  ratio = ratio * (float(elem[counter]) / float(elem[-2]))
                  counter -= 1
              statesalary = .71 * (ratio)**((9-originalcounter)/4) * basesalary
              projectedsalarylist.append(statesalary)
              elemcounter += 1
              if elemcounter == 51:
                  break
      return projectedsalarylist
  else:
      for elem in data.json():
          if str(elem[-1]) == statenumbers[states.index(area)]:
              ratio = 1 + increase_rate
              if 'B20004_001E' in census_variables:
                  ratio = ratio * (float(elem[census_variables.index('B20004_001E')-1])/ float(elem[census_variables.index('B20004_001E')]))
                  counter -= 1
              while counter:
                  ratio = ratio * (float(elem[counter]) / float(elem[-2]))
                  counter -= 1
              return ratio*basesalary
          #int(str(elem[1]))

allstatelist = blah(basesalary)
print "Your projected salary is " + str(numpy.mean(allstatelist)) + "."
