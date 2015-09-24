'''
Created on 2015年9月23日

@author: zhou
'''
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(file_name):
    try:
        with open(file_name)as athlete:
            return(athlete).readline().strip().split(',')
#             data = athlete.readline()
#             return(data.strip().split(','))
    except IOError as err:
        print('File error:' + str(err))
        return None