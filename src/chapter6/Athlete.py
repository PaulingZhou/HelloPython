'''
Created on 2015年10月3日

@author: zhou
'''
import chapter6

class Athlete(object):
    '''
    classdocs
    '''


    def __init__(self, a_name, a_dob=None, a_times=[]):
        '''
        Constructor
        '''
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        
    def top3(self):
        '''
        Return size of self
        '''
        return(sorted(set([chapter6.sanitize.sanitize(t) for t in self.times]))[0:3])
    
    def add_time(self,timeVal):
        self.times.append(timeVal)
        
    def add_times(self,timeList):
        self.times.extend(timeList)
        
class nameList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name
        
class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__(self)
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
        
    def top3(self):
        return(sorted(set([chapter6.sanitize.sanitize(t) for t in self]))[0:3])
    
    def add_time(self,time_value):
        self.append(time_value)
        
    def add_times(self,time_list):
        self.extend(time_list)