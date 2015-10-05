#!/usr/local/bin/python3
import cgitb
cgitb.enable()
'''
Created on 2015年10月5日

@author: zhou
'''
import cgi
import athletemodel
import yate

# Get the data from the model
athletes = athletemodel.get_from_store()
# Which athlete's data are you working with?

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete: " + athlete_name +\
                   ",DOB: " + athletes[athlete_name].dob + "."))
print(yate.para("The top times for this athlete are: "))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"Home": "/index.html",\
                          "Select another athlete": "geneate_list.py"}))
