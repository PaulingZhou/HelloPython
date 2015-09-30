'''
Created on 2015年9月30日

@author: zhou
'''
import os
from chapter6.sanitize import sanitize,get_coach_data
os.chdir("hfpy_ch6_data")
sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))