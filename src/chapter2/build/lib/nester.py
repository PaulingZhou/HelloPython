'''
Created on 2015年9月17日
This is the "nester.py"module, and it provides one function called print_lol() which prints list that may or 
may not include nest lists.
@author: zhou
'''
        
        
def print_lol(the_list,level):
    
    '''
    This function takes a positional argument called "the_list", which is any Python list(of ,possibly, nested lists).
    Each data item in the providedlist is (recursively) printed to the screen on its own line.
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
                print('\t', end='')
            print(each_item)
