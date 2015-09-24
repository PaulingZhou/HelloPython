'''
Created on 2015年9月23日

@author: zhou
'''
import os
from chapter5.sanitize import sanitize, get_coach_data
os.chdir('hfpy_ch5_data')
try:
    #===========================================================================
    # with open('james.txt','r') as out_james:
    #     james = out_james.readline().strip().split(',')
    # with open('julie.txt','r') as out_julie:
    #     julie = out_julie.readline().strip().split(',')
    # with open('mikey.txt','r') as out_mikey:
    #     mikey = out_mikey.readline().strip().split(',')
    # with open('sarah.txt','r') as out_sarah:
    #     sarah = out_sarah.readline().strip().split(',')
    #===========================================================================
    
    #===========================================================================
    # clean_james = []
    # clean_julie = []
    # clean_mikey = []
    # clean_sarah = []
    # 
    # for each_t in james:
    #     clean_james.append(sanitize(each_t))
    # for each_t in julie:
    #     clean_julie.append(sanitize(each_t))
    # for each_t in mikey:
    #     clean_mikey.append(sanitize(each_t))
    # for each_t in sarah:
    #     clean_sarah.append(sanitize(each_t))
    #===========================================================================
    
    #===========================================================================
    # '''
    # list comprehension
    # '''
    # james = sorted([sanitize(each_t) for each_t in james])
    # julie = sorted([sanitize(each_t) for each_t in julie])
    # mikey = sorted([sanitize(each_t) for each_t in mikey])
    # sarah = sorted([sanitize(each_t) for each_t in sarah])
    # 
    # unique_james = []
    # unique_julie = []
    # unique_mikey = []
    # unique_sarah = []
    # 
    # for each_item in james:
    #     if each_item not in unique_james:
    #         unique_james.append(each_item)
    # for each_item in julie:
    #     if each_item not in unique_julie:
    #         unique_julie.append(each_item)
    # for each_item in mikey:
    #     if each_item not in unique_mikey:
    #         unique_mikey.append(each_item)
    # for each_item in sarah:
    #     if each_item not in unique_sarah:
    #         unique_sarah.append(each_item)
    # print(unique_james[0:3])
    # print(unique_julie[0:3])
    # print(unique_mikey[0:3])
    # print(unique_sarah[0:3])
    #===========================================================================
    james = get_coach_data('james.txt')
    julie = get_coach_data('julie.txt')
    mikey = get_coach_data('mikey.txt')
    sarah = get_coach_data('sarah.txt')
    '''
    use set
    '''
    print(sorted(set([sanitize(t) for t in james]))[0:3])
    print(sorted(set([sanitize(t) for t in julie]))[0:3])
    print(sorted(set([sanitize(t) for t in mikey]))[0:3])
    print(sorted(set([sanitize(t) for t in sarah]))[0:3])
    
    
except IOError as err:
    print('File error' + str(err))