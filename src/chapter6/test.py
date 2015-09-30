'''
Created on 2015年9月30日

@author: zhou
'''
import os
from chapter6.sanitize import sanitize,get_coach_data
os.chdir("hfpy_ch6_data")
sarah = get_coach_data('sarah2.txt')
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
print(james['Name'] + "'s fastest times are: " + james['Times'])
print(julie['Name'] + "'s fastest times are: " + julie['Times'])
print(mikey['Name'] + "'s fastest times are: " + mikey['Times'])
print(sarah['Name'] + "'s fastest times are: " + sarah['Times'])

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