'''
Created on 2015年9月20日

@author: zhou
'''
# import os
# print(os.getcwd())
import Print
import pickle

man = []
other = []
try:
    data = open('sketch.txt')
    # print(data.readline(),end='')
    # print(data.readline(),end='')
    # data.seek(0)
    for each_line in data:
    #     if not each_line.find(':') == -1:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
#             print(role, end='')
#             print(' said: ', end='')
#             print(line_spoken, end='')
        except ValueError:
            pass
#             print(each_line,end='')    
    #     print(each_line,end='')
    data.close
except IOError:
    print('the data file is missing')
# print(man)
# print(other)

#===============================================================================
# try:
#     out_man = open('man_data.txt','w')
#     out_other = open('other_data.txt','w')
#     print(man, file = out_man)
#     print(other, file = out_other)
# #     out_man.close
# #     out_other.close
# except IOError as err:
#     print('file error' + str(err))
# finally:
#     if 'out_man' in locals():
#         out_man.close
#     if 'out_other' in locals():
#         out_other.close   
#===============================================================================

#===============================================================================
# try:
#     with open('man_data.txt','w') as out_man:
#         Print.print_lol(man, fh = out_man)
# #         print(man, file = out_man)
#     with open('other_data.txt','w') as out_other:
#         Print.print_lol(other, fh = out_other)
# #         print(other, file = out_other) 
# except IOError as err:
#     print('file error: ' + str(err))
# with open('man_data.txt') as mdf:
#     print(mdf.readline())
# #     Print.print_lol(man, fh = out_man)
#===============================================================================

try:
    with open('man_data.txt','wb') as out_man,open('other_data','wb') as out_other:
        pickle.dump(man, out_man)
        pickle.dump(other, out_other)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('PickleError: ' + str(perr))
    
new_man = []
try:
    with open('man_data.txt', 'rb') as man_file, open('other_data', 'rb') as other_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('PickleError: ' + str(perr))
Print.print_lol(new_man)
print(new_man)