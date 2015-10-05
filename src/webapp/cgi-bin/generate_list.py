#! /usr/local/bin/python3
'''
Created on 2015年10月4日

@author: zhou
'''


#===============================================================================
# '''
# code of model
# '''
# import os
# from chapter7.athletemodel import put_to_store, get_from_store
# os.chdir("hfpy_ch6_data")
# the_files = ['sarah2.txt','james2.txt','mikey2.txt','julie2.txt']
# data = put_to_store(the_files)
# print(data)
# for each_athlete in data:
#     print(data[each_athlete].name + ' ' + data[each_athlete].dob)
# data_copy = get_from_store()
# for each_athlete in data_copy:
#     print(data_copy[each_athlete].name + '' + data_copy[each_athlete].dob)
#===============================================================================

#===============================================================================
# '''
# code of view
# '''
# from chapter7.yate import start_response, include_footer,u_list
# print(start_response())
# print(start_response('text/plain'))
# print(start_response('application/json'))
# print(include_footer({'Home': '/index.html', 'Select': '/cgi-bin/select.py'}))
# print(u_list(['Life of Brian', 'Holy Grail']))
#===============================================================================

import glob
import athletemodel
import yate

data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_files)
print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form("generating_timeing_data.py"))
print(yate.para("Select an athlete from the list to work with:"))

for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))
