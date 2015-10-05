'''
Created on 2015年9月30日

@author: zhou
'''
import os
from chapter6.sanitize import get_coach_data
from chapter6.Athlete import Athlete, nameList
import chapter6
os.chdir("hfpy_ch6_data")
sarah = get_coach_data('sarah2.txt')
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
print(james.name)
print(james.name + "'s fastest times are: " + str(james.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
# 
# vera = Athlete('Vera')
# vera.add_time('1.32')
# print(vera.top3())
# vera.add_times(['2.11','1-30','1:31'])
# print(vera.top3())
# print(james['Name'] + "'s fastest times are: " + james['Times'])
# print(julie['Name'] + "'s fastest times are: " + julie['Times'])
# print(mikey['Name'] + "'s fastest times are: " + mikey['Times'])
# print(sarah['Name'] + "'s fastest times are: " + sarah['Times'])

# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
# sarah_data = {'Name': sarah.pop(0), 'DOB': sarah.pop(0), 'Times': sarah}
# print(sarah_data['Name'] + "'s fastest times are:" + \
#       str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))

#===============================================================================
# palin = dict()
# print(type(palin))
#===============================================================================

#===============================================================================
# cleese = {}
# cleese['Name'] = 'John Cleese'
# cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
# palin = {'Name': 'Michael Palin', 'Occupations' : ['comedian', 'actor', 'writer', 'tv']}
# # print(palin['Name'])
# # print(cleese['Occupations'][-1])
# palin['Birthplace'] = 'Broomhill, Sheffield, England'
# cleese['Birthplace'] = 'Weston-super-Mare, North Somerest, England'
# print(palin)
# print(cleese) 
#===============================================================================

#===============================================================================
# johnney = nameList("John Paul Jones")
# # print(type(johnney))
# # print(dir(johnney))
# johnney.append('Bass Player')
# johnney.extend(['Composor','Arranger','Musician'])
# print(johnney.name)
# for attr in johnney:
#     print(johnney.name + " is a " + attr + ".")
#===============================================================================

vera = chapter6.Athlete.AthleteList('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['1-30','1:29','1:45'])
print(vera.top3())